def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_absolute_value(n):
    if n < 0:
        return -n
    elif n > 0:
        return n
