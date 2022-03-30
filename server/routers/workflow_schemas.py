from typing import Optional, List, Dict

from pydantic import BaseModel

class WorkflowModel(BaseModel):
    searchtwitter : Dict["text": str, "keywords": List[str], "tones": List[str], "startime": str, "endtime": str]
    

class Workflow(BaseModel):
    user_id: str
    workflow: List[WorkflowModel]