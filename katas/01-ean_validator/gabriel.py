def validate_ean(code):
    checksum = 0
    for index, digit in enumerate(code[:-1]):
        index += 1
        int_digit = int(digit)
        checksum += int_digit        
        if index % 2 == 0:
            checksum += int_digit*2
    return str(10 - (checksum % 10))[-1] == code[-1]

