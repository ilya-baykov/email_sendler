import os
from loguru import logger

# Определяем корневой путь проекта
root_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем папку LOGS, если она не существует
log_dir = os.path.join(root_dir, "../LOGS")
os.makedirs(log_dir, exist_ok=True)

logger.add(
    os.path.join(log_dir, "log_{time:YYYY-MM-DD}.log"),  # Логи за день
    rotation="1 day",  # Ротация по дням
    retention="7 days",  # Хранить логи за 7 дней
    compression="zip",  # Архивировать логи
    level="DEBUG",  # Уровень логирования
    format="{time:MM-DD at HH:mm:ss} | {level} | {message} | {name}:{function}:{line}"  # Формат сообщения
)
