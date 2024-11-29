"""
Идеята е да се премахват най-големите числа първо,
затова и речника започва с най големите римски.

Обхождат се (num, roman) двойките от речника и
докато num се съдържа в числото 'n', num se вади
от n и се конкатенира римската репрезентация
на num към резултата

Greedy
"""

LARGEST_CONVERTABLE_NUMBER = 3999

INT_TO_ROMAN_DICT = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I',
}


def convert_to_roman(n) -> str:
    if n > LARGEST_CONVERTABLE_NUMBER:
        raise ValueError(f'The largest convertable number is {LARGEST_CONVERTABLE_NUMBER}')

    res = ''
    for num, roman in INT_TO_ROMAN_DICT.items():
        while n >= num:
            res += roman
            n = n - num

    return res
