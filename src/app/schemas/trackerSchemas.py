from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from src.app.model.trackerModel import HabitCategoryEnum , StatusEnum

class TrackerReturnSchema(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    category: HabitCategoryEnum
    goal: str
    status: StatusEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


