from fastapi import APIRouter , Depends
from app.model.trackerModel import Habit
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_session
from sqlalchemy.future import select
from app.schemas.trackerSchemas import TrackerReturnSchema , CreateHabitSchema
from typing import List
from app.service.service import post_habit , get_all_habits , get_habit, update_habit , delete_habit

router = APIRouter(prefix="/habit", tags=["habit"])


@router.post("/" , response_model=TrackerReturnSchema)
async def post_habit_handler(schema: CreateHabitSchema , session: AsyncSession = Depends(get_session)):
    return await post_habit(
        session=session,
        schema=schema)

@router.get("/" , response_model=List[TrackerReturnSchema])
async def get_all_habits_handler(session: AsyncSession = Depends(get_session)):
    return await get_all_habits(
        session=session
    )

@router.get("/{habit_id}" , response_model=TrackerReturnSchema)
async def get_habit_handler(habit_id : str , session: AsyncSession = Depends(get_session)):
    return get_habit(
        habit_id = habit_id,
        session=session
    )

@router.put("/{habit_id}" , response_model=TrackerReturnSchema)
async def update_habit_handler(habit_id : str , schema: CreateHabitSchema , session: AsyncSession = Depends(get_session)):
    return await update_habit(
        habit_id = habit_id,
        session=session,
        schema=schema
    )

@router.delete("/{habit_id}" , response_model=dict)
async def delete_habit_handler(habit_id : str , session: AsyncSession = Depends(get_session)):
    return await delete_habit(
        habit_id = habit_id,
        session=session
    )
