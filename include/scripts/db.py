import psycopg2
import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def save_to_neon(final_state):
    """
    Persists agent findings (metadata, markdown, and summaries) 
    into the Neon Postgres database.
    """
    # establish conn 
    conn = psycopg2.connect(os.getenv("NEON_DATABASE_URL"))
    cur = conn.cursor()

    # extract the data from langgraph state 
    papers_metadata = final_state.get("papers_metadata" , [])
    parsed_docs = final_state.get("parsed_docs", [])
    summaries = final_state.get("final_summaries", [])


    for i , metadata in enumerate(papers_metadata):
        cur.execute("""
        INSERT INTO research_knowledge_base 
            (arxiv_id, title, full_text_markdown, ai_summary)
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (arxiv_id) DO NOTHING
        """),(
            meta['id'], 
            meta['title'], 
            parsed_docs[i] if i < len(parsed_docs) else None, 
            summaries[i] if i < len(summaries) else None
        )
        # 4. Commit and Close
    conn.commit()
    cur.close()
    conn.close()
    print(f"Successfully saved {len(papers_metadata)} papers to Neon.")
