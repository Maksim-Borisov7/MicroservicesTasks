import asyncio
from repositories.tasks import TaskRepository
from logs.logger import logger


class StartTaskUseCase:
    """Use-case для запуска задачи."""
    def __init__(self, repo: TaskRepository):
        """Инициализация use-case с указанием репозитория."""
        self.repo = repo

    async def execute(self, data: dict):
        """Запустить задачу по ID."""
        task_id: str = data["task_id"]
        logger.info(
            f"START: запрос на запуск задачи {task_id}"
        )
        task = await self.repo.get_task_by_id(task_id)
        if not task:
            logger.warning(
                f"START: задача {task_id} не найдена"
            )
            return {
                "task_id": task_id,
                "status": "not_found"
            }

        if task.status in ["running", "ready", "error"]:
            logger.info(
                f"START: задача {task_id} уже в статусе '{task.status}'"
            )
            return {
                "task_id": task_id,
                "status": task.status
            }

        await self.repo.update_result(
            task_id,
            result=None,
            status="running"
        )
        logger.info(
            f"START: задача {task_id} запущена"
        )

        _ = asyncio.create_task(self.process_fibonacci(task.n, task.id))
        return {"task_id": task_id, "status": task.status}

    async def process_fibonacci(
            self,
            n: int,
            task_id: str
    ):
        """Фоновое вычисление Fibonacci."""
        try:
            logger.info(
                f"PROCESS: вычисление Fibonacci({n})"
            )

            result = await asyncio.to_thread(self.fibonacci,  n)
            logger.info(
                f"PROCESS: задача {task_id} завершена, результат={result}"
            )
            await self.repo.update_result(
                task_id,
                result,
                status="ready"
            )
        except Exception as e:
            logger.error(
                f"PROCESS: ошибка задачи {task_id}: {e}",
                exc_info=True
            )

            await self.repo.update_result(
                task_id,
                result=None,
                status="error"
            )

    @classmethod
    def fibonacci(cls, n: int):
        if n <= 1:
            return n
        else:
            return cls.fibonacci(n - 1) + cls.fibonacci(n - 2)
