
def power1(base, exponent):

    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = power1(base, exponent >>1)
    result *= result
    if exponent & 1 ==1:
        result *= base
    return result

print(power1(2,16))

