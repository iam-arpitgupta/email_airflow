from typing import TypedDict
from typing import Typing , Dict , List , Annotated
import operator 

class AgentState(TypedDict):
    arxiv_ids : List[str]
    papers_metadata : List[dict]
    parsed_docs: Annotated[List[str], operator.add]
    final_reports: List[str]


    

