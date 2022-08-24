# Часть 1
#   Задание 1
print("Задание 1.1")
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    if end < start:
        raise Exception("range is incorrect")
except Exception as e:
    if e.__str__() == "range is incorrect":
        temp = end
        end = start
        start = temp
    else:
        exit(-1)
except:
    exit(-1)

i = start + 1
while i < end:
    if i % 7 == 0:
        print(i)
    i += 1

#   Задание 2
print("Задание 1.2")
while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if end < start:
            temp = end
            end = start
            start = temp
        break
    except:
        print("Повторите попытку")
print("Все числа диапазона: ")
for i in range(start + 1, end):
    print(i, end=" ")
print("\nВсе числа диапазона в убывающем порядке: ")
for i in range(end - 1, start, -1):
    print(i, end=" ")
print("\nВсе числа, кратные 7: ")
for i in range(start + 1, end):
    if i % 7 == 0:
        for j in range(i, end, 7):
            print(j, end=" ")
        break
print("\nЧисел, кратных 5: ")
amount = 0
for i in range(start + 1, end):
    if i % 5 == 0:
        amount += 1
print(amount)

#   Задание 3
print("Задание 1.3")
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    step = 1
    if end < start:
        start -= 2
        step = -1
except:
    print("Диапазон выбран автоматически [0, 10]")
    start = 0
    end = 10
    step = 1

for i in range(start + 1, end, step):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Часть 2
#   Задание 1
print("Задание 2.1")
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    if end < start:
        temp = end
        end = start
        start = temp
except:
    print("Диапазон выбран автоматически [0, 10]")
    start = 0
    end = 10
even_num_sum = 0
even_num_amt = 0
odd_num_sum = 0
odd_num_amt = 0
multiples_9_sum = 0
multiples_9_amt = 0
for i in range(start + 1, end):
    if i % 2 == 0:
        even_num_sum += i
        even_num_amt += 1
    else:
        odd_num_sum += i
        odd_num_amt += 1
    if i % 9 == 0:
        multiples_9_sum += i
        multiples_9_amt += 1
print("Cумма четных чисел в указанном диапазоне: ", even_num_sum)
if even_num_amt != 0:
    print("Среднеарифметическое: ", even_num_sum / even_num_amt)
else:
    print("Среднеарифметическое: 0")
print("Cумма  нечетных чисел в указанном диапазоне: ", odd_num_sum)
if odd_num_amt != 0:
    print("Среднеарифметическое: ", odd_num_sum / odd_num_amt)
else:
    print("Среднеарифметическое: 0")
print("Cумма чисел кратных 9 в указанном диапазоне: ", multiples_9_sum)
if multiples_9_amt != 0:
    print("Среднеарифметическое: ", multiples_9_sum / multiples_9_amt)
else:
    print("Среднеарифметическое: 0")

#   Задание 2
print("Задание 2.2")
try:
    line_length = int(input("Введите длину линии: "))
    symbol = input("Введите символ для заполнения линии: ")
except:
    print("Длина линии и символ выбраны автоматически: 10 *")
    line_length = 10
    symbol = "*"
i = 0
while i < line_length:
    print(symbol)
    i += 1

# Задание 3
print("Задание 2.3")
print("Для завершения работы программы введите 7")
while True:
    try:
        number = int(input("Введите число: "))
        if number == 7:
            print("Good bye!")
            break
        if number < 0:
            print("Number is negative")
        elif number > 0:
            print("Number is positive")
        else:
            print("Number is equal to zero")
    except:
        print("Повторите попытку")

#   Задание 4
print("Задание 2.4")
print("Для прекращения ввода чисел и завершения работы программы введите 7")
total = 0
is_first_time = True
while True:
    try:
        if is_first_time:
            number = int(input("Введите число: "))
            if number == 7:
                print("Good bye!")
                break
            total += number
            max_mun = number
            min_num = number
            is_first_time = False
        else:
            number = int(input("Введите следующее число: "))
            if number == 7:
                print(f"Сумма: {total}\nMax: {max_mun}\nMin: {min_num}")
                print("Good bye!")
                break
            total += number
            if max_mun < number:
                max_mun = number
            elif min_num > number:
                min_num = number
    except:
        print("Повторите попытку")

# Часть 3
#   Задание 1
print("Задание 3.1")
while True:
    try:
        x = int(input("Введите основание степени: "))
        y = int(input("Введите показатель степени: "))
        extent = 1
        i = 0
        while i < abs(y):
            extent *= x
            i += 1
        if y < 0:
            extent = 1 / extent
        print(f"{x}^{y}={extent}")
        break
    except ZeroDivisionError:
        print("Ноль в отрицательную степень возводить нельзя")
    except:
        print("Повторите попытку")

#   Задание 2
print("Задание 3.2")
amount = 0
for i in range(100, 1000):
    # print(i)
    _1 = i // 100
    _2 = i % 100 // 10
    _3 = i % 10
    # print(_1, _2, _3)
    if _1 == _2 or _1 == _3 or _2 == _3:
        # print(i, end=" ")
        amount += 1
print("\nВсего в диапазоне [100, 999] ", amount, " целых чисел у которых есть две одинаковые цифры")

#   Задание 3
print("Задание 3.3")
amount = 0
for i in range(100, 10000):
    _1 = i // 1000
    _2 = i % 1000 // 100
    _3 = i % 100 // 10
    _4 = i % 10
    # print(_1, _2, _3, _4)
    if i < 1000:
        if _2 != _3 and _2 != _4 and _3 != _4:
            # print(i, end=" ")
            amount += 1
    else:
        if _1 != _2 and _1 != _3 and _1 != _4 and _2 != _3 and _2 != _4 and _3 != _4:
            # print(i, end=" ")
            amount += 1
print("\nВсего в диапазоне [100, 9999] ", amount, " целых чисел у которых все цифры разные")

#   Задание 4
print("Задание 3.4")
while True:
    try:
        number = int(input("Введите любое целое число: "))
        temp = number
        new_number = ""
        while temp > 0:
            digit = temp % 10
            if digit != 3 and digit != 6:
                new_number = str(digit) + new_number
            temp = temp // 10
        if new_number != "":
            number = int(new_number)
        else:
            number = 0
        print("Стало:\t", number)
        break
    except:
        print("Повторите попытку")
