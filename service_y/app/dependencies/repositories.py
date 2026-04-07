from faststream import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import database
from repositories.tasks import TaskRepository


def get_task_repo(
        session: AsyncSession = Depends(database.get_session),
) -> TaskRepository:
    """
    Создаёт и возвращает экземпляр TaskRepository с переданной сессией БД.

    Используется как зависимость FastAPI (`Depends`) для эндпоинтов,
    где нужен доступ к репозиторию задач.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy, предоставляемая через Depends.

    Returns:
        TaskRepository: Экземпляр репозитория задач, привязанный к сессии.
    """
    return TaskRepository(session)
