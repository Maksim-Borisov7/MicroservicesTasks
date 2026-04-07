from datetime import datetime
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для всех ORM-моделей SQLAlchemy."""
    pass


class TaskModels(Base):
    """
        ORM-модель задачи.

        Хранит:
        - идентификатор задачи
        - результат вычисления
        - статус выполнения
        - входное число n
        - дату создания
    """
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(primary_key=True)
    result: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(
        String,
        default="created",
        nullable=False
    )
    n: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
