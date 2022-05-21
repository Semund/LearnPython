"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    now_datetime = datetime.now()
    timedelta_1day = timedelta(days=1)
    timedelta_30days = timedelta(days=30)
    datetime_format = "%d.%m.%Y %A %H:%M:%S"
    print('Today: ', datetime.strftime(now_datetime, datetime_format))
    print('Yesterday: ', datetime.strftime(now_datetime - timedelta_1day, datetime_format))
    print('30 days ago: ', datetime.strftime(now_datetime - timedelta_30days, datetime_format))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    datetime_from_string = str_2_datetime("01/01/20 12:10:03.234567")
    print(datetime_from_string, type(datetime_from_string), sep=' : ')
