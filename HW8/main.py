import random

test_list = [random.randint(0, 10) for i in range(0, 5)]
print(f"test_list: {test_list}")


# Задание 1
def multiply_elem(int_list):
    mult = 1
    for elem in int_list:
        mult *= elem
    return mult


print("Задание 1: ", multiply_elem(test_list))


# Задание 2
def min_elem(int_list):
    # return min(int_list)
    min_e = int_list[0]
    for i in range(1, len(int_list)):
        if int_list[i] < min_e:
            min_e = int_list[i]
    return min_e


print("Задание 2: ", min_elem(test_list))


# Задание 3
def is_prime(num):
    if 1 < num:
        for d in range(2, num // 2 + 1):
            if num % d == 0:
                return False
        return True
    else:
        return False


def prime_count(int_list):
    count = 0
    for e in int_list:
        if is_prime(e):
            count += 1
    return count


print("Задание 3: ", prime_count(test_list))


# Задание 4
def delete_elems(int_list, dlt_value):
    count = 0
    for e in int_list:
        if e == dlt_value:
            int_list.remove(dlt_value)
            count += 1
    return count


print("Задание 4: ", delete_elems(test_list, 3))
print(test_list)


# Задание 5
def unite_lists(list1, list2):
    return list1 + list2


second_list = [random.randint(10, 20) for i in range(0, 5)]
print(f"second_list: {second_list}")

unt_list = unite_lists(test_list, second_list)
print("Задание 5: ", unt_list)


# Задание 6
def exponentiate_elem(int_list, exponent):
    exp_list = []
    for e in int_list:
        exp_list.append(e ** exponent)
    return exp_list


power_list = exponentiate_elem(test_list, 2)
print("Задание 6: ", power_list)
