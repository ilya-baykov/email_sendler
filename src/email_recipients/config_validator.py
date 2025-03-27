import pandas as pd
import re

from src.email_recipients.exeptions import *
from configs.logger import logger


class EmailsFileValidator:
    """Класс для валидации настроечного файла с получателями рассылки."""

    def __init__(self, file_path: str):
        """
        Инициализация класса.

        :param file_path: Путь к Excel-файлу с адресами электронной почты.
        """
        self.file_path = file_path

    @staticmethod
    def __is_valid_email(email: str) -> bool:
        """
        Проверка на корректность адреса электронной почты.

        :param email: Адрес электронной почты для проверки.
        :return: True, если адрес корректен, иначе False.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def __is_valid_extension_file(self) -> None:
        """
        Проверка, что файл имеет расширение .xls или .xlsx.

        :raises InvalidFileTypeError: Если файл не является Excel-файлом.
        """
        if not (self.file_path.endswith('.xls') or self.file_path.endswith('.xlsx')):
            raise InvalidFileTypeError("Файл должен быть в формате Excel (.xls или .xlsx).")

    def validate(self) -> None:
        """
        Проверка адресов электронной почты в Excel-файле.

        :raises EmptyFileError: Если файл пустой.
        :raises MissingColumnError: Если столбец 'Email' не найден.
        :raises InvalidEmailError: Если адрес электронной почты некорректен.
        :raises InvalidFileTypeError: Если файл не является Excel-файлом.
        """
        # Проверка расширения файла
        self.__is_valid_extension_file()

        try:
            # Чтение Excel-файла
            df = pd.read_excel(self.file_path)

            # Проверка, что файл не пустой
            if df.empty:
                raise EmptyFileError("Файл пустой.")

            # Проверка, что в файле есть столбец 'Email'
            if 'Email' not in df.columns:
                raise MissingColumnError("Столбец 'Email' не найден.")

            # Проверка каждого адреса электронной почты
            for index, email in df['Email'].items():
                if self.__is_valid_email(email):
                    logger.debug(f"Адрес электронной почты '{email}' на строке {index + 1} корректен.")
                else:
                    raise InvalidEmailError(f"Адрес электронной почты '{email}' на строке {index + 1} некорректен.")

        except (EmptyFileError, MissingColumnError, InvalidEmailError) as e:
            logger.error(f"Ошибка: {e}")
            raise
        except Exception as e:
            logger.exception("Произошла ошибка: %s", e)
            raise
