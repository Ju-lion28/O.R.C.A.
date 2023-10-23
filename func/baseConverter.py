def base_conversion(number, source_base, target_base):
    decimal_number = 0

    # Convert from the source base to decimal
    for digit in str(number):
        if digit.isnumeric():
            digit_value = int(digit)
        else:
            digit_value = ord(digit.upper()) - ord("A") + 10
        decimal_number = decimal_number * source_base + digit_value

    result = ""

    # Convert from decimal to the target base
    while decimal_number > 0:
        remainder = decimal_number % target_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord("A") + remainder - 10) + result
        decimal_number = decimal_number // target_base

    return result
