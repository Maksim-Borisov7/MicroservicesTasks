from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TaskResult(BaseModel):
    """
    Модель результата задачи.

    Атрибуты:
        id (str): Уникальный идентификатор задачи.
        n (int): Параметр задачи (например, n-ое число Фибоначчи).
        result (Optional[int]): Результат вычисления задачи (если завершена успешно).
        status (str): Статус задачи: created, running, ready, error.
        created_at (Optional[datetime]): Время создания задачи.
    """
    # model_config = ConfigDict(from_attributes=True)

    id: str = Field(..., description="Идентификатор задачи")
    n: int = Field(..., description="Параметр задачи (например, n-ое число Фибоначчи)")
    result: Optional[int] = Field(None, description="Результат вычисления задачи")
    status: str = Field(..., description="Статус выполнения задачи")
    created_at: Optional[datetime] = Field(None, description="Время создания задачи")


class TasksResponse(BaseModel):
    """
    Модель ответа со списком задач.

    Атрибуты:
        tasks (List[TaskResult]): Список всех задач.
    """
    tasks: list[TaskResult] = Field(..., description="Список всех задач")


