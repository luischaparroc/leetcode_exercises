

def isPalindrome(x: int) -> bool:
    string_x = ''
    input_number = abs(x)

    while input_number:
        string_x = chr(input_number % 10) + string_x
        input_number //= 10

    if x < 0:
        string_x = '-' + string_x

    return string_x == string_x[::-1]