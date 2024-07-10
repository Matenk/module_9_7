def is_prime(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        if r < 0:
            return 'Нет'
        if r == 1:
            return 'нет'
        elif r == 2:
            return 'Простое'
        else:
            for i in range(2, int(r ** 0.5)+1):
                if r % i == 0:
                    return 'Составное'
            return 'Простое'



    return wrapper


@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c


result = sum_three(2, 3, 6)
print(result)