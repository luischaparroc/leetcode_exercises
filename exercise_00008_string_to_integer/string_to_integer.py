

def myAtoi(s: str) -> int:
    s = s.lstrip()

    if not s:
        return 0

    output = 0
    sign_number = 1
    first_character = s[0]

    if '0 ' <= first_character <= '9':
        output += int(first_character)
    elif first_character == '-':
        sign_number = -1
    elif first_character != '+':
        return output

    for character in s[1:]:
        if character < '0' or character > '9':
            break
        output = output * 10 + int(character)

    output *= sign_number
    min_number = -2 ** 31
    max_number = (2 ** 31) - 1

    if output < min_number:
        return min_number

    if output > max_number:
        return max_number

    return output
