from typing import Optional

from email_sendler.email_sender_with_attachments import EmailSenderWithAttachments
from email_sendler.email_sender_without_attachments import EmailSenderWithoutAttachments


class EmailService:
    """Фасадный класс для работы с почтой. Выбирает нужный класс отправителя."""

    def __init__(self, login_mail: str, password_mail: str):
        self.sender_without_attachments = EmailSenderWithoutAttachments(login_mail, password_mail)
        self.sender_with_attachments = EmailSenderWithAttachments(login_mail, password_mail)

    def send_email(self, subject: str, body: str, mail_to: list[str],
                   copy_recipients: Optional[list[str]] = None,
                   attachments: Optional[list[str]] = None):
        """
        Отправка email.

        В зависимости от наличия вложений метод автоматически выбирает соответствующий класс для отправки письма.

        :param subject: Тема письма
        :param body: Текст письма
        :param mail_to: Список получателей
        :param copy_recipients: Список получателей копии (опционально)
        :param attachments: Список файлов для вложений (опционально)
        """
        if attachments:
            self.sender_with_attachments.send(subject, body, mail_to, copy_recipients, attachments)
        else:
            self.sender_without_attachments.send(subject, body, mail_to, copy_recipients)
