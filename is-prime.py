import math

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, num//2 +1):
        if num % i == 0:
            return False
    return True