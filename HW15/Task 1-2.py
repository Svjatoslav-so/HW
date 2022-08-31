import time


# Task 1
class MeasureTimeDecorator:
    def __init__(self, func):
        self.func = func

    # измеряет время выполнения функции (в секундах)
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        return end - start, result


# возвращает True, если число k простое, иначе - False
def is_prime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False

    return True


@MeasureTimeDecorator
def get_prime_numbers():
    return [num for num in range(1000) if is_prime(num)]


primelist = get_prime_numbers()
# print(len(primelist), '%.15f' % primelist[0], len(primelist[1]), primelist[1])
print('Time: %.5f' % primelist[0], "\nAmount of prime numbers:", len(primelist[1]))


# Task 2
@MeasureTimeDecorator
def get_prime_numbers_in_range(start, end):
    return [num for num in range(start, end) if is_prime(num)]


prime_in_range = get_prime_numbers_in_range(-100, 1000000)
# print(len(prime_in_range), prime_in_range)
print('Time: %.5f' % prime_in_range[0], "\nAmount of prime numbers:", len(prime_in_range[1]))
