from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.model.trackerModel import HabitCategoryEnum , StatusEnum
from uuid import UUID


class TrackerReturnSchema(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    category: HabitCategoryEnum
    goal: str
    status: StatusEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CreateHabitSchema(BaseModel):
    name: str
    description: Optional[str] = None
    category: HabitCategoryEnum
    goal: str
    status: StatusEnum


