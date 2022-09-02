# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#

import os

# получить число с консоли
#   message - сообщение для пользователя
from distutils.command.clean import clean


def get_int(message: str) -> int:
    return int(input(message))

# сообщает выходной день, или нет
# если указан недействительный номер дня недели
# возвращает пустую строку
#   day_no - номер дня недели
def day_is_dayoff(day_no: int) -> str:
    result = ''

    if day_no in range(1,6):
        result = 'будний'
    elif day_no in range(6,8):
        result = 'выходной'

    return result


os.system('cls')
day_no = get_int('Введите номер дня недели: ')
day_name = day_is_dayoff(day_no)

if day_name == '':
    print('Неверный номер дня')
else:
    print(f'{day_no} - {day_name} день')