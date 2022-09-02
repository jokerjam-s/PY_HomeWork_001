# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os

# получить число с консоли
#   message - сообщение для пользователя
def get_int(message: str) -> int:
    return int(input(message))


## MAIN ## 
arr_coord = [
    'x=(0 .. ꝏ), y=(0 .. ꝏ)',
    'x=(0 .. -ꝏ), y=(0 .. ꝏ)',
    'x=(0 .. -ꝏ), y=(0 .. -ꝏ)',
    'x=(0 .. ꝏ), y=(0 .. -ꝏ)']

os.system('cls')

quoter = get_int('Ведеите номер четверти: ')
if quoter not in range(1,5):
    print('неверные данные')
else:
    print(f'диапазон координат {arr_coord[quoter-1]}')