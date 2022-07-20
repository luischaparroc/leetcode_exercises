

ROMAN_NUMBERS = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}


def int_to_roman(num: int) -> str:

    roman_number = ''
    target_integer = 0
    target_letter = ''

    while num > 0:

        for integer, letter in ROMAN_NUMBERS.items():
            if integer > num:
                break
            target_integer = integer
            target_letter = letter

        while num >= target_integer:
            roman_number += target_letter
            num -= target_integer

    return roman_number
