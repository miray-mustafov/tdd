"""
Идеята е да се премахват най-големите числа първо,
затова и речника започва с най големите римски.

Обхождат се (num, roman) двойките от речника и
докато num се съдържа в числото 'n', num se вади
от n и се конкатенира римската репрезентация
на num към резултата

Greedy
"""

largest_convertable_number = 3999


def convert_to_roman(n) -> str:
    if n > largest_convertable_number:
        raise ValueError(
            f'The largest convertable number is {largest_convertable_number}'
        )
    d = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I',
    }
    res = ''
    for num, roman in d.items():
        while n >= num:
            res += roman
            n = n - num
    return res
