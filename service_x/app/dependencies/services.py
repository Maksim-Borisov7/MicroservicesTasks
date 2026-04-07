from services.task import TaskService
from broker.broker_client import BrokerClient


def get_task_service() -> TaskService:
    """Возвращает готовый TaskService"""
    broker_client = BrokerClient()
    return TaskService(broker_client=broker_client)
