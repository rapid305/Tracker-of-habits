from fastapi import APIRouter , Depends
from app.model.trackerModel import Habit
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_session
from sqlalchemy.future import select
from app.schemas.trackerSchemas import TrackerReturnSchema , CreateHabitSchema
from typing import List

router = APIRouter(prefix="/habit", tags=["habit"])


@router.post("/" , response_model=TrackerReturnSchema)
async def post_habit(schema: CreateHabitSchema , session: AsyncSession = Depends(get_session)):
    new_habit = Habit(**schema.model_dump())
    session.add(new_habit)
    await session.commit()
    await session.refresh(new_habit)
    return TrackerReturnSchema.model_validate(new_habit)

@router.get("/{habit_id}" , response_model=TrackerReturnSchema)
async def get_habit(habit_id : str , session: AsyncSession = Depends(get_session)):
    query = select(Habit).where(Habit.id == habit_id)
    result = await session.execute(query)
    habit = result.scalars().first()
    if not habit:
        return {"error": "Habit not found"}
    return TrackerReturnSchema.model_validate(new_habit)

@router.get("/" , response_model=List[TrackerReturnSchema])
async def get_all_habits(session: AsyncSession = Depends(get_session)):
    query = select(Habit).order_by(Habit.id)
    result = await session.execute(query)
    get_habits = result.scalars().all()
    return [TrackerReturnSchema.model_validate(habit) for habit in get_habits]


