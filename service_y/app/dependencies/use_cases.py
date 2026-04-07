from faststream import Depends
from dependencies.repositories import get_task_repo
from repositories.tasks import TaskRepository
from use_case.create_task import CreateTaskUseCase
from use_case.start_task import StartTaskUseCase
from use_case.get_all_task import GetAllTaskUseCase
from logs.logger import logger


def get_create_task_use_case(repo: TaskRepository = Depends(get_task_repo)):
    """
    Создаёт и возвращает экземпляр use-case для создания новой задачи.

    Args:
        repo (TaskRepository): Репозиторий задач, предоставленный через Depends.

    Returns:
        CreateTaskUseCase: Use-case для создания новой задачи.
    """
    logger.info("Создаю CreateTaskUseCase...")
    return CreateTaskUseCase(repo)


def get_start_task_use_case(repo: TaskRepository = Depends(get_task_repo)):
    """
    Создаёт и возвращает экземпляр use-case для запуска задачи.

    Args:
        repo (TaskRepository): Репозиторий задач, предоставленный через Depends.

    Returns:
        StartTaskUseCase: Use-case для запуска задачи.
    """
    logger.info("Создаю StartTaskUseCase...")
    return StartTaskUseCase(repo)


def get_all_task_use_case(repo: TaskRepository = Depends(get_task_repo)):
    """
    Создаёт и возвращает экземпляр use-case для получения списка задач.

    Args:
        repo (TaskRepository): Репозиторий задач, предоставленный через Depends.

    Returns:
        GetAllTaskUseCase: Use-case для получения списка задач.
    """
    logger.info("Создаю GetAllTaskUseCase...")
    return GetAllTaskUseCase(repo)
