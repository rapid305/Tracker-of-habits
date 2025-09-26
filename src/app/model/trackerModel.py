from src.app.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String , func , Enum as SqlAlchemyEnum
from enum import Enum

class HabitCategoryEnum(str , Enum):
    HEALTH = "health"
    PRODUCTIVITY = "productivity"
    PERSONAL_DEVELOPMENT = "personal_development"
    SOCIAL = "social"
    HOBBIES = "hobbies"
    FINANCE = "finance"
    OTHER = "other"

class StatusEnum(str  , Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    COMPLETED = "completed"

class Habit(Base):
    __tablename__ = "habit"

    id: Mapped[int] = mapped_column(
        String(36) ,
        primary_key=True ,
        index=True ,
        server_default=func.uuid_generate_v7()
    )
    name: Mapped[str] = mapped_column(
        String(255) ,
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        String(255) ,
        nullable=True
    )
    category: Mapped[HabitCategoryEnum] = mapped_column(
        SqlAlchemyEnum(HabitCategoryEnum) ,
        nullable=False
    )
    goal: Mapped[str] = mapped_column(
        String(255) ,
        nullable=False
    )
    status: Mapped[StatusEnum] = mapped_column(
        SqlAlchemyEnum(StatusEnum) ,
        nullable=False ,
        default=StatusEnum.ACTIVE
    )
    created_at: Mapped[str] = mapped_column(
        String(255) ,
        nullable=False ,
        server_default=func.now()
    )
    updated_at: Mapped[str] = mapped_column(
        String(255) ,
        nullable=False ,
        server_default=func.now() ,
        onupdate=func.now()
    )
