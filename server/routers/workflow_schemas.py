from typing import Optional, List

from pyparsing import Dict
from pydantic import BaseModel

class WorkflowModel(BaseModel):
    searchtwitter : Dict["text": str, "startime": str, "endtime": str]
    

class Workflow(BaseModel):
    user_id: str
    workflow: list[WorkflowModel]