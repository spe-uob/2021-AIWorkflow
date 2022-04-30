from typing import Optional, List, Dict

from pydantic import BaseModel


class WorkflowRun(BaseModel):
    user_id: str
    workflow: dict
