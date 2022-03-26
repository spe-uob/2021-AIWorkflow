from typing import Optional, List
from pydantic import BaseModel

class WorkflowModel(Basemodel):
    searchtwitter = {"text": str, "startime": str, "endtime": str}
    

class Workflow(BaseModel):
    user_id: str
    workflow: list[WorkflowModel]