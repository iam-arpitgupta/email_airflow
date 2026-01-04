from langgraph.graph import StateGraph, START, END
from include.agents.state import fetch_papers_node, docling_parse_node, summarize_expert_node
from include.agents.state import AgentState
def create_research_graph():
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("fetcher", fetch_papers_node)
    workflow.add_node("parser", docling_parse_node)
    workflow.add_node("summarizer", summarize_expert_node)
    
    # Define Edges (Start -> Fetch -> Parse -> Summarize -> End)
    workflow.add_edge(START, "fetcher")
    workflow.add_edge("fetcher", "parser")
    workflow.add_edge("parser", "summarizer")
    workflow.add_edge("summarizer", END)
    
    return workflow.compile()