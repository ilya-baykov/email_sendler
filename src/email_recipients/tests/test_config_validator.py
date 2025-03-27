# src/email_recipients/tests/test_config_validator.py

import pytest
import pandas as pd
from unittest.mock import patch

from src.email_recipients.config_validator import EmailsFileValidator
from src.email_recipients.exeptions import *


class TestEmailsFileValidator:

    def test_is_valid_email(self, email_validator):
        assert email_validator._EmailsFileValidator__is_valid_email("test@example.com") is True
        assert email_validator._EmailsFileValidator__is_valid_email("invalid-email") is False
        assert email_validator._EmailsFileValidator__is_valid_email("another.test@domain.co") is True
        assert email_validator._EmailsFileValidator__is_valid_email("test@.com") is False

    @patch('pandas.read_excel')
    def test_validate_empty_file(self, mock_read_excel, email_validator):
        mock_read_excel.return_value = pd.DataFrame()  # Пустой DataFrame

        with pytest.raises(EmptyFileError, match="Файл пустой."):
            email_validator.validate()

    @patch('pandas.read_excel')
    def test_validate_missing_email_column(self, mock_read_excel, email_validator):
        mock_read_excel.return_value = pd.DataFrame({'OtherColumn': ['value1', 'value2']})  # Нет столбца 'Email'

        with pytest.raises(MissingColumnError, match="Столбец 'Email' не найден."):
            email_validator.validate()

    @patch('pandas.read_excel')
    def test_validate_invalid_email(self, mock_read_excel, email_validator):
        mock_read_excel.return_value = pd.DataFrame({'Email': ['valid@example.com', 'invalid-email']})

        with pytest.raises(InvalidEmailError, match="Адрес электронной почты 'invalid-email' на строке 2 некорректен."):
            email_validator.validate()

    def test_validate_invalid_file_type(self):
        with pytest.raises(InvalidFileTypeError, match="Файл должен быть в формате Excel (.xls или .xlsx)."):
            EmailsFileValidator("invalid_file.txt").validate()

    @patch('pandas.read_excel')
    def test_validate_correct_file(self, mock_read_excel, email_validator):
        mock_read_excel.return_value = pd.DataFrame({'Email': ['valid@example.com', 'another.valid@example.com']})

        try:
            email_validator.validate()  # Не должно вызывать исключений
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {e}")
