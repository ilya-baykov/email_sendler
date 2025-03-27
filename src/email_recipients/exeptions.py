class EmailError(Exception):
    """Базовый класс для ошибок, связанных с адресами электронной почты."""
    pass


class EmptyFileError(EmailError):
    """Ошибка, возникающая, когда файл пустой."""
    pass


class MissingColumnError(EmailError):
    """Ошибка, возникающая, когда отсутствует столбец 'Email'."""
    pass


class InvalidEmailError(EmailError):
    """Ошибка, возникающая, когда адрес электронной почты некорректен."""
    pass


class InvalidFileTypeError(Exception):
    """Ошибка, возникающая, когда файл имеет расширение отличное от Экселя."""
    pass
