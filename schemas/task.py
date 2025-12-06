from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


class TaskBaseSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    user_name: str = Field(..., min_length=1, max_length=100)
    body: str = Field(default="", max_length=500)
    end_date: datetime


class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=150)
    user_name: Optional[str] = Field(None, min_length=1, max_length=100)
    body: Optional[str] = Field(None, max_length=500)
    end_date: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)


class TaskReadSchema(TaskBaseSchema):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
