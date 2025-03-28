from abc import ABC, abstractmethod
from typing import Optional

from email_sendler.exceptions import EmailCredentialsError


class AbstractEmailSender(ABC):
    """Абстрактный класс для отправки email-сообщений."""

    def __init__(self, login_mail: str, password_mail: str):
        """
        Инициализация отправителя email.

        :param login_mail: Логин для SMTP
        :param password_mail: Пароль для SMTP
        """
        if not login_mail or not password_mail:
            raise EmailCredentialsError("Ошибка: Необходимо указать EMAIL_LOGIN и EMAIL_PASSWORD.")

        self.login_mail = login_mail
        self.password_mail = password_mail

    @abstractmethod
    def send(self, subject: str, body: str, mail_to: list[str], copy_recipients: Optional[list[str]] = None):
        """Абстрактный метод для отправки email."""
        pass
