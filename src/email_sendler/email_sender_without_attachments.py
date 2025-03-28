import smtplib

from email.message import EmailMessage
from typing import Optional

from configs.logger import logger
from configs.email_constants import *
from email_sendler.abstract_email_sender import AbstractEmailSender


class EmailSenderWithoutAttachments(AbstractEmailSender):
    """Класс для отправки email без вложений."""

    def send(self, subject: str, body: str, mail_to=list[str], copy_recipients: Optional[list[str]] = None):
        """
        Отправка email без вложений.

        :param subject: Тема письма
        :param body: Текст письма
        :param mail_to: Адрес получателя (или список адресов)
        :param copy_recipients: Адрес получателя (или список адресов) для копии
        """

        msg = EmailMessage()
        msg["From"] = MAIL_FROM
        msg["To"] = mail_to
        if copy_recipients:
            msg["Cc"] = copy_recipients
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(self.login_mail, self.password_mail)
                server.send_message(msg)
            logger.info("Письмо отправлено успешно без вложений.")
        except Exception as e:
            logger.error(f"Ошибка при отправке письма без вложений: {e}")
