from typing import Optional, List, Dict

from pydantic import BaseModel

class GetWorkflowRequest(BaseModel):
    workflow_id: int

class GetWorkflowResponse(BaseModel):
    workflow: str
