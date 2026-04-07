from typing import Annotated
from fastapi import APIRouter, Depends
from dependencies.services import get_task_service
from services.task import TaskService
from schemas.request import TaskCreate, TaskStart
from schemas.response import TaskResponse, TasksListResponse

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create", response_model=TaskResponse, status_code=201)
async def create_task(
        data: TaskCreate,
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    """Создает задачу в микросервисе Y"""
    return await task_service.create(data)


@router.post("/start", response_model=TaskResponse, status_code=202)
async def start_task(
        data: TaskStart,
        task_service: TaskService = Depends(get_task_service)
):
    """Асинхронный запуск задачи"""
    return await task_service.start(data)


@router.get("/get", response_model=TasksListResponse, status_code=200)
async def get_all_tasks(task_service: TaskService = Depends(get_task_service)):
    """Получает список всех задач"""
    return await task_service.get_all()
