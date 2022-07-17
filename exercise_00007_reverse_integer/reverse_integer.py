

def reverse(x: int) -> int:
    input_number = abs(x)
    output_number = 0

    while input_number != 0:
        mod = input_number % 10
        output_number = (output_number * 10) + mod
        input_number //= 10

    if x < 0:
        output_number *= -1

    pow_limit_number = 2 ** 31

    if output_number < pow_limit_number * -1 or output_number > pow_limit_number - 1:
        output_number = 0

    return output_number
