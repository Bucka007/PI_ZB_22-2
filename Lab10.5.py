from datetime import datetime


class InvalidDateFormatError(Exception):
    """
    Исключение, возникающее при неверном формате даты
    """
    pass


def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def check_date_format(date_str):
    if not is_valid_date_format(date_str):
        raise InvalidDateFormatError("Неверный формат даты")


def process_data(date_str):
    try:
        check_date_format(date_str)
        # ... обработка данных ...
    except InvalidDateFormatError as e:
        print(f"Ошибка: {e}")


# Тесты

date_str = "2023-12-32"
try:
    process_data(date_str)
except InvalidDateFormatError as e:
    print(f"Ошибка: {e}")

date_str = "2024-04-03"
process_data(date_str)