from fastapi import HTTPException
from broker.broker_client import BrokerClient
from logs.logger import logger
from schemas.request import TaskCreate, TaskStart
from schemas.response import TaskResponse, TasksListResponse, TaskError


class TaskService:
    """
    Сервисный слой для работы с задачами в service_x.

    Отвечает за коммуникацию с service_y через RabbitMQ.
    """

    def __init__(self, broker_client: BrokerClient):
        """Инициализация сервиса"""
        self.broker_client = broker_client

    @staticmethod
    def _handle_error(operation: str, e: Exception) -> None:
        """Централизованная обработка ошибок"""
        logger.error(f"{operation}: {e}", exc_info=True)

        raise HTTPException(
            status_code=503,
            detail=TaskError(
                error=operation,
                detail=str(e)
            ).model_dump()
        )

    async def create(self, data: TaskCreate) -> TaskResponse:
        """Создать задачу"""
        logger.info(f"Получен запрос на создание задачи: n={data.n}")
        try:
            parsed_data = await self.broker_client.request_and_parse(
                message={"n": data.n},
                queue="create"
            )
            logger.info(f"Задача успешно создана и выполнена. Результат: {parsed_data.get('result')}")
            return TaskResponse(**parsed_data)
        except Exception as e:
            self._handle_error("Не удалось создать задачу", e)

    async def start(self, data: TaskStart) -> TaskResponse:
        """Запустить задачу асинхронно"""
        logger.info(f"Получен запрос на запуск задачи: task_id={data.task_id}")
        try:
            parsed_data = await self.broker_client.request_and_parse(
                message={"task_id": data.task_id},
                queue="start"
            )
            if parsed_data.get("status") == "not_found":
                code = parsed_data.get("code", 404)
                raise HTTPException(status_code=code, detail=parsed_data.get("error"))

            logger.info(f"Задача {data.task_id} успешно запущена. Статус: {parsed_data.get('status')}")
            return TaskResponse(**parsed_data)

        except HTTPException:
            raise
        except Exception as e:
            self._handle_error("Не удалось запустить задачу", e)

    async def get_all(self) -> TasksListResponse:
        """Получить список всех задач."""
        logger.info("Получен запрос на получение списка всех задач")
        try:
            data = await self.broker_client.request_and_parse(
                message={},
                queue="get_all"
            )

            if isinstance(data, list):
                logger.info(f"Получен список задач")
                return TasksListResponse(tasks=data)

            logger.info(f"Получен список задач")
            return TasksListResponse(**data) if isinstance(data, dict) else TasksListResponse(tasks=[])

        except Exception as e:
            self._handle_error("Не удалось получить список задач", e)
