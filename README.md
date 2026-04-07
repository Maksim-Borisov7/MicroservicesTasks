## microservices-task-system — Микросервисная система асинхронной обработки задач

### О проекте

Проект состоит из двух микросервисов:

- **Service X** — FastAPI приложение. Принимает HTTP-запросы от пользователей и делегирует тяжёлые задачи через RabbitMQ.
- **Service Y** — FastStream worker, который выполняет ресурсоёмкие вычисления, сохраняет задачи и их результаты в PostgreSQL.

### Технологический стек

- **Backend**: Python 3.10
- **API**: FastAPI
- **Async Worker**: FastStream + RabbitMQ
- **База данных**: PostgreSQL + SQLAlchemy (async)
- **Контейнеризация**: Docker, Docker Compose
- **Валидация**: Pydantic 
- **Логирование**: logging

## Этапы запуска проекта:
### 1) Клонирование репозитория:
```python
git clone https://github.com/Maksim-Borisov7/MicroservicesTasks.git

```

### 2) переходим в папку командой:
```python 
cd ifra
```

### 3) Настройка переменных окружения
+ Создайте файл .env в папке /infra 
+ Скопируйте содержимое папки .env.example в .env

### 4) Запуск проекта 
```python 
docker compose up --build
```

### 5) После запуска приложение доступно по адресу:
+ Fastapi http://localhost:8000/docs
+ RabbitMQ http://localhost:15672/


### 6) Остановка контейнеров
```python 
docker compose down
```