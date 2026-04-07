import json
from typing import Any, Dict
from fastapi import HTTPException
from faststream.rabbit import RabbitMessage
from broker.core import broker


class BrokerClient:
    """Клиент для работы с RabbitMQ"""

    @staticmethod
    async def request_and_parse(
        message: Dict[str, Any],
        queue: str,
        timeout: float = 30.0
    ) -> Dict[str, Any]:
        """Отправляет запрос и автоматически парсит ответ"""
        try:
            response: RabbitMessage = await broker.request(
                message=message,
                queue=queue,
                timeout=timeout
            )
            body = response.body

            if isinstance(body, bytes):
                body = body.decode("utf-8")

            if not body:
                raise ValueError(f"Пустой ответ от очереди '{queue}'")

            data = json.loads(body)
            return data

        except json.JSONDecodeError:
            raise HTTPException(
                status_code=502,
                detail=f"Service Y вернул некорректный JSON из очереди '{queue}'"
            )
        except Exception as e:
            raise HTTPException(
                status_code=503,
                detail=f"Ошибка связи с Service Y (очередь '{queue}'): {str(e)}"
            )
