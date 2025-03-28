# src/email_recipients/tests/conftest.py
from unittest.mock import patch

import pytest

from src.email_recipients.config_validator import EmailsFileValidator
from src.email_recipients.email_recipients import EmailRecipients


@pytest.fixture
def email_validator():
    """Фикстура для создания экземпляра EmailsFileValidator."""
    return EmailsFileValidator("dummy_path.xlsx")


@pytest.fixture
def email_recipients():
    """Фикстура для создания экземпляра EmailRecipients без вызова валидации."""
    with patch.object(EmailsFileValidator, 'validate', return_value=None):
        yield EmailRecipients("dummy_path.xlsx")
