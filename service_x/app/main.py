from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.tasks import router as tasks_router
from logs.logger import logger
from broker.core import init_broker, close_broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Контекстный менеджер жизненного цикла FastAPI."""
    try:
        logger.info("Starting Service X")
        await init_broker()
        yield
        await close_broker()
        logger.info("Service X stopped")
    except Exception as e:
        logger.error(f"Failed to start Service X: {e}", exc_info=True)
        raise


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
