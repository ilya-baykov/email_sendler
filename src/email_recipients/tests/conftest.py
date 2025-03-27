# src/email_recipients/tests/conftest.py

import pytest

from src.email_recipients.config_validator import EmailsFileValidator


@pytest.fixture
def email_validator():
    """Фикстура для создания экземпляра EmailsFileValidator."""
    return EmailsFileValidator("dummy_path.xlsx")
