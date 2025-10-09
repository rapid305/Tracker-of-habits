from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.trackerSchemas import TrackerReturnSchema , CreateHabitSchema
from app.model.trackerModel import Habit
from sqlalchemy.future import select


async def post_habit(session: AsyncSession, schema: CreateHabitSchema) -> TrackerReturnSchema:
    new_habit = Habit(**schema.model_dump())
    await session.add(new_habit)
    await session.commit()
    await session.refresh(new_habit)
    return TrackerReturnSchema.model_validate(new_habit)

async def get_all_habits(session: AsyncSession) -> list[TrackerReturnSchema]:
    result = await session.execute(select(Habit).order_by(Habit.id))
    get_habits = result.scalars().all()
    return [TrackerReturnSchema.model_validate(habit) for habit in get_habits]

async def get_habit(session: AsyncSession, habit_id : str) -> TrackerReturnSchema | dict:
    result = await session.execute(select(Habit).where(Habit.id == habit_id))
    habit = result.scalars().first()
    if not habit:
        return {"error": "Habit not found"}
    return TrackerReturnSchema.model_validate(habit)

async def update_habit(session: AsyncSession, habit_id : str , schema: CreateHabitSchema) -> TrackerReturnSchema | dict:
    result = await session.execute(select(Habit).where(Habit.id == habit_id))
    habit = result.scalars().first()
    if not habit:
        return {"error": "Habit not found"}
    for key, value in schema.model_dump().items():
        setattr(habit, key, value)
    await session.commit()
    await session.refresh(habit)
    return TrackerReturnSchema.model_validate(habit)

async def delete_habit(session: AsyncSession, habit_id : str) -> dict:
    result = await session.execute(select(Habit).where(Habit.id == habit_id))
    habit = result.scalars().first()
    if not habit:
        return {"error": "Habit not found"}
    await session.delete(habit)
    await session.commit()
    return {"message": "Habit deleted successfully"}