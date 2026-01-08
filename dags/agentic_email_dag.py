from datetime import datetime , timedelta
from airflow.sdk import dag, task
from include.scripts.db import save_to_neon
from include.agents.graph import create_research_graph
from include.scripts.utils import send_research_email

@dag(
    dag_id="agentic_researcher_v3",
    start_date=datetime(2026, 1, 1),
    schedule="0 8 * * *",        # Every morning at 8:00 AM
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    }
)


def run_agent_pipeline():
    @task 
    def trigger_agent():
        """Run the langgraph agent this will get the arxiv paper and then summerize it """
        app = create_research_agent()
        initalize_state = {"papers_metadata": [], "parsed_docs": [], "final_summaries": []}
        final_state = app.invoke(initalize_state)
        return final_state
        

    @task 
    def store_data(final_state):
        """Store the summerized data into neon DB """
        save_to_neon(final_state)
        return final_state
    

    @task 
    def email_report(final_state):
        """Task 3: Send the email summary"""
        if final_state["final_summaries"]:
            top_paper = final_state["papers_metadata"][0]
            send_research_email(
                summary_text=final_state["final_summaries"][0],
                paper_title=top_paper['title'],
                paper_url=top_paper.get('url', 'https://arxiv.org')
            )

    # Dependency Flow
    state = trigger_agent()
    stored_state = store_data(state)
    email_report(stored_state)

run_agent_pipeline()




