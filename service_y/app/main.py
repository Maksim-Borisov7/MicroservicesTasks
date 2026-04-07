import asyncio
from contextlib import asynccontextmanager
from faststream import FastStream
from database.db import database
from logs.logger import logger
from broker.core import init_broker, close_broker, broker
import api.subscribers


@asynccontextmanager
async def lifespan():
    """Контекстный менеджер жизненного цикла FastStream."""
    logger.info("Starting Service Y")
    try:
        await database.create_table()
        await init_broker()
        yield
        await close_broker()
        logger.info("Service Y stopped")
    except Exception as e:
        logger.error(f"Failed to start Service Y: {e}", exc_info=True)
        raise


app = FastStream(broker, lifespan=lifespan)

if __name__ == "__main__":
    asyncio.run(app.run())
