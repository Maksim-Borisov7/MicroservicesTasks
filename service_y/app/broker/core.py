from faststream.rabbit import RabbitBroker
from config import settings
from logs.logger import logger

broker = RabbitBroker(settings.rabbitmq_url)


async def init_broker():
    """Подключение брокера"""
    await broker.connect()
    logger.info("RabbitMQ broker connected")


async def close_broker():
    """Завершение работы брокера"""
    await broker.stop()
    logger.info("RabbitMQ broker disconnected")