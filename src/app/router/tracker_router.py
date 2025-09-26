from fastapi import APIRouter , Depends
from src.app.model import Habit
from fastapi.ext.asyncio import AsyncSesion
from src.app.database.database import get_session
from sqlalchemy.future import select
from src.app.schemas.trackerSchemas import TrackerReturnSchema


router = APIRouter(prefix="/habit", tags=["habit"])


@router.post("/" , response_model=TrackerReturnSchema)
async def post_habit(schema: TrackerReturnSchema , session: AsyncSesion = Depends(get_session)):
    new_habit = Habit(**schema.model_dump())
    session.add(new_habit)
    await session.commit()
    await session.refresh(new_habit)
    return await new_habit

@router.get("/{habit_id}" , response_model=TrackerReturnSchema)
async def get_habit(habit_id : str , session: AsyncSesion = Depends(get_session)):
    query = select(Habit).where(Habit.id == habit_id)
    result = await session.execute(query)
    new_habit = result.scalars().first()
    return await new_habit

@router.get("/" , response_model=List[TrackerReturnSchema])
async def get_all_habits(session: AsyncSesion = Depends(get_session)):
    query = select(Habit).order_by(Habit.id)
    result = await session.execute(query)
    get_habits = result.scalars().all()
    return await [TrackerReturnSchema.model_validate(get_habits) for habit in get_habits]


