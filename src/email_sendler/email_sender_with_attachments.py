import smtplib
import os
import mimetypes

from email.message import EmailMessage
from typing import Optional

from configs.logger import logger
from email_sendler.abstract_email_sender import AbstractEmailSender
from configs.email_constants import *


class EmailSenderWithAttachments(AbstractEmailSender):
    """Класс для отправки email с вложениями."""

    def send(self, subject: str, body: str, attachments: list,
             mail_to=list[str], copy_recipients: Optional[list[str]] = None):
        """
        Отправка email с вложениями.

        :param subject: Тема письма
        :param body: Текст письма
        :param attachments: Список файлов для вложения
        :param mail_to: Адрес получателя (или список адресов)
        :param copy_recipients: Optional[list[str]] = None
        """

        msg = EmailMessage()
        msg["From"] = MAIL_FROM
        msg["To"] = mail_to
        if copy_recipients:
            msg["Cc"] = copy_recipients
        msg["Subject"] = subject
        msg.set_content(body)

        for file_path in attachments:
            if not os.path.exists(file_path) or os.path.getsize(file_path) > MAX_FILE_SIZE:
                logger.warning(f"Пропуск вложения {file_path}: файл слишком большой или не существует.")
                continue

            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or "application/octet-stream"
            maintype, subtype = mime_type.split("/", 1)

            with open(file_path, "rb") as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(file_path))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(self.login_mail, self.password_mail)
                server.send_message(msg)
            logger.info("Письмо отправлено успешно с вложениями.")
        except Exception as e:
            logger.error(f"Ошибка при отправке письма с вложениями: {e}")
