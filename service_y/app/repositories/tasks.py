from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import TaskModels

from logs.logger import logger


class TaskRepository:
    """
    Репозиторий для работы с задачами.

    Отвечает за:
    - создание задач
    - получение задач
    - обновление результатов
    """

    model = TaskModels

    def __init__(self, session: AsyncSession):
        """
        Инициализация репозитория.

        Args:
            session (AsyncSession): Асинхронная сессия SQLAlchemy для работы с БД.
        """
        self.session = session

    async def create_task(
            self,
            task_id: str,
            n: int
    ) -> TaskModels:
        """
        Создать новую задачу.
        Args:
            task_id (str): ID задачи
            n (int): входное значение
        Returns:
            TaskModels: созданная задача
        """

        logger.info(
            f"DB: создание задачи {task_id} (n={n})"
        )
        try:
            task = self.model(
                id=task_id,
                n=n
            )
            self.session.add(task)
            await self.session.commit()
            logger.info(
                f"DB: задача {task_id} создана"
            )
            return task

        except Exception as e:
            logger.error(
                f"DB: ошибка создания задачи {task_id}: {e}",
                exc_info=True
            )
            raise

    async def get_task_by_id(
            self,
            task_id: str
    ) -> TaskModels | None:
        """Получить задачу по ID."""
        logger.info(
            f"DB: получение задачи {task_id}"
        )
        try:
            query = select(self.model).where(
                self.model.id == task_id
            )
            res = await self.session.execute(query)
            task = res.scalar_one_or_none()
            return task

        except Exception as e:
            logger.error(
                f"DB: ошибка получения задачи {task_id}: {e}",
                exc_info=True
            )
            raise

    async def update_result(
            self,
            task_id: str,
            result: int | None,
            status: str
    ) -> None:
        """Обновить результат задачи."""
        logger.info(
            f"DB: обновление задачи {task_id}, status={status}"
        )
        try:
            query = (
                update(self.model)
                .where(self.model.id == task_id)
                .values(
                    result=result,
                    status=status
                )
            )
            await self.session.execute(query)
            await self.session.commit()

        except Exception as e:
            logger.error(
                f"DB: ошибка обновления задачи {task_id}: {e}",
                exc_info=True
            )
            raise

    async def get_tasks(self) -> list[TaskModels]:
        """Получить список всех задач."""
        logger.info(
            "DB: получение всех задач"
        )
        try:
            query = select(self.model)
            res = await self.session.execute(query)
            tasks: list[TaskModels] = list(res.scalars().all())
            return tasks

        except Exception as e:
            logger.error(
                f"DB: ошибка получения списка задач: {e}",
                exc_info=True
            )
            raise






