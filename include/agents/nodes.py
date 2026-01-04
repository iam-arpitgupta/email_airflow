# dockling -> for the processing purpose 
from include.agents.state import AgentState
import arxiv 
from dockling.document_convertor import DocumentConvertor 
import google.generativeai as genai 

def fetch_paper_nodes(state : AgentState):
    client = arxiv.Client()
    search = arxiv.Search(query = "cat:cs.AI",max_results = 2)
    results = [{"id": r.entry_id.split('/')[-1], "url": r.pdf_url, "title": r.title} 
               for r in client.results(search)]
    return {"papers_metadata": results}


def dockling_parse_node(state : AgentState):
    convertor = DocumentConvertor()
    batch_markdown = []
    for paper in state["papers_metadata"]:
        # Docling converts URL directly to clean Markdown
        result = converter.convert(paper["url"])
        batch_markdown.append(result.document.export_to_markdown())
    return {"parsed_docs": batch_markdown}


    # 3. Summarizer Node
def summarize_expert_node(state):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-3-Thinking')
    batch_summaries = []
    
    for text in state["parsed_docs"]:
        prompt = f"Summarize this research paper Markdown for a CTO. Focus on innovations:\n\n{text[:15000]}"
        res = model.generate_content(prompt)
        batch_summaries.append(res.text)
    return {"final_summaries": batch_summaries}
