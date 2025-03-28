from unittest.mock import patch
from pytest import mark

import pandas as pd


class TestEmailRecipients:

    @patch('pandas.read_excel')
    @mark.parametrize(
        ["file_contents", "result"],
        [
            ({'Email': ['ilya.baykov@rt.ru']}, ['ilya.baykov@rt.ru']),

            ({'Email': ['ilya.baykov@rt.ru', 'astemir.dyshekov@rt.ru']},
             ['ilya.baykov@rt.ru', 'astemir.dyshekov@rt.ru'])
        ]
    )
    def test_get_recipients_list(self, mock_read_excel, email_recipients, file_contents, result):
        # Настройка замоканного метода read_excel
        mock_read_excel.return_value = pd.DataFrame(file_contents)

        # Вызов метода, который будет использовать замоканный read_excel
        recipients_list = email_recipients.get_recipients_list()

        # Проверка результата
        assert recipients_list == result
