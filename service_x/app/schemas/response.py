from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field


class TaskResponse(BaseModel):
    """Ответ от сервиса Y"""
    status: str = Field(..., description="Статус выполнения задачи")
    task_id: str = Field(..., description="Идентификатор задачи")


class TaskResult(BaseModel):
    """Результат, который Y отправляет обратно"""
    id: str
    n: int
    result: Optional[int] = None
    status: str
    created_at: Optional[datetime] = None


class TasksListResponse(BaseModel):
    """Ответ на /get endpoint (список всех задач)"""
    tasks: List[TaskResult]


class TaskError(BaseModel):
    """Модель ошибки"""
    error: str = Field(..., description="Сообщение об ошибке")
    detail: Optional[str] = Field(None, description="Дополнительная информация")
