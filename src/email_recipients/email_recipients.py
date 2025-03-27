from typing import Optional

import pandas as pd

from configs.logger import logger
from src.email_recipients.config_validator import EmailsFileValidator


class EmailRecipients:
    """Класс для работы с получателями email-рассылки"""

    def __init__(self, file_path: str):
        """
        Инициализация класса
        :param file_path:Путь до настроечного файла с получателями email-рассылки
        """
        self.file_path = file_path
        self.validator = EmailsFileValidator(file_path)
        self.validator.validate()  # Валидация при инициализации

    def get_recipients_list(self) -> list[str]:
        """Получить список получателей рассылки."""
        recipients_list = self.__read_recipients_file()
        return recipients_list

    def __read_recipients_file(self) -> Optional[list[str]]:
        """Чтение файла получателей и возврат списка адресов электронной почты."""
        try:
            emails = pd.read_excel(self.file_path)
            recipients_list = emails['Email'].dropna().astype(str).tolist()
            return recipients_list
        except Exception as e:
            logger.error(f"Ошибка при чтении файла получателей: {e}")
            return []
