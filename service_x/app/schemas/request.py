from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Запрос на создание задачи"""
    n: int = Field(..., gt=0, description="Число для вычисления задачи")


class TaskStart(BaseModel):
    """Запрос на вычисление задачи"""
    task_id: str = Field(..., description="Идентификатор задачи")