def is_prime(func):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                print('составное')
        print('простое')
        return x
    return wrapper


@is_prime
def sum_three(a, b, c):
    summ = a+b+c
    return summ


result = sum_three(2, 3, 6)
print(result)
