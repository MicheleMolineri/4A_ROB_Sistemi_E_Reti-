def check(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len(digits) == 0:
        return [0]

def rebase(input_base, digits, output_base):
    
    check(input_base, digits, output_base)
    
    base_ten_num = base_ten(input_base, digits)
    if base_ten_num == 0:
        return [0]
    
    result = []
    while base_ten_num > 0:
        result.append(base_ten_num % output_base)
        base_ten_num = base_ten_num // output_base
    result.reverse()
    return result


def base_ten(input_base, digits):
    exponent = 0
    i , base_ten_num= len(digits) - 1, 0
    
    while i >= 0:
        if digits[i] < 0 or digits[i] >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        base_ten_num += digits[i] * (input_base ** exponent)
        exponent += 1
        i -= 1
    return base_ten_num