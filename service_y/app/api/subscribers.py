from dependencies.use_cases import get_start_task_use_case
from broker.core import broker
from use_case.start_task import StartTaskUseCase
from faststream import Depends
from use_case.create_task import CreateTaskUseCase
from dependencies.use_cases import get_create_task_use_case, get_all_task_use_case
from use_case.get_all_task import GetAllTaskUseCase
from schemas.task import TasksResponse
from logs.logger import logger


@broker.subscriber("create")
async def create_task(
        data: dict,
        use_case: CreateTaskUseCase = Depends(get_create_task_use_case)
):
    """Создание новой задачи через брокера."""
    logger.info(f"CREATE: получен запрос, n={data['n']}")
    return await use_case.execute(data)


@broker.subscriber("start")
async def start_task(
        data: dict,
        use_case: StartTaskUseCase = Depends(get_start_task_use_case)
):
    """Запуск задачи через брокера."""
    logger.info(f"START: получен запрос, n={data.get('n')}")
    return await use_case.execute(data)


@broker.subscriber("get_all")
async def get_all(
        use_case: GetAllTaskUseCase = Depends(get_all_task_use_case)
) -> TasksResponse:
    """Получение задач через брокера."""
    logger.info(f"GET_ALL: получен запрос")
    return await use_case.execute()



