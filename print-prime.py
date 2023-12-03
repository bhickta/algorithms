def print_prime(num: int):
    ret = []
    for n in range(2, num):
        if is_prime(n):
            ret.append(n)
    return ret
            

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1): # or i * i <= num
        if num % i == 0:
            return False
    return True

print(print_prime(30))