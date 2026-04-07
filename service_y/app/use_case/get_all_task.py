from repositories.tasks import TaskRepository
from schemas.task import TaskResult, TasksResponse
from logs.logger import logger


class GetAllTaskUseCase:
    """Use-case для получения списка всех задач."""
    def __init__(self, repo: TaskRepository):
        """Инициализация use-case с указанием репозитория."""
        self.repo = repo

    async def execute(self) -> TasksResponse:
        """Получить список всех задач."""
        try:
            tasks = await self.repo.get_tasks()
            logger.info(
                f"GET_ALL: выполнение получения задач из БД"
            )

            task_responses = [
                TaskResult.model_validate(task, from_attributes=True)
                for task in tasks
            ]
            logger.info(
                f"GET_ALL: Задачи успешно преобразованы"
            )

            return TasksResponse(tasks=task_responses)

        except Exception as e:
            logger.error(
                f"GET_ALL: ошибка при получении задач: {e}",
                exc_info=True
            )
            raise
