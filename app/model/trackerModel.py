from app.database.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String , func , Enum as SqlAlchemyEnum
from enum import Enum
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


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

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(
        String(255) ,
        nullable=False,
        index=True
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
    created_at: Mapped[datetime] = mapped_column(
        String(255) ,
        nullable=False ,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        String(255) ,
        nullable=False ,
        server_default=func.now() ,
        onupdate=func.now()
    )
