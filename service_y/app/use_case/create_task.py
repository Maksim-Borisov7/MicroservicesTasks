import uuid
from repositories.tasks import TaskRepository
from logs.logger import logger


class CreateTaskUseCase:
    """Use-case для создания задачи."""
    def __init__(self, repo: TaskRepository):
        """Инициализация use-case с указанием репозитория."""
        self.repo = repo

    async def execute(self, data: dict):
        """Создать задачу"""
        try:
            task_id = str(uuid.uuid4())
            n = data["n"]

            await self.repo.create_task(task_id, n)

            logger.info(f"Задача создана: id={task_id}, n={n}")

            return {"task_id": task_id, "status": "created"}

        except Exception as e:
            logger.error(f"Ошибка create_task: {e}", exc_info=True)
            raise

