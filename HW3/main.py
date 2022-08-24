
# Задание 1
print("\nЗадание 1")
user_value = int(input("Введите число в диапазоне от 1 до 100: "))
if 1 <= user_value <= 100:
    if user_value % 3 == 0:
        print("Fizz")
        if user_value % 5 == 0:
            print("Buzz")
    elif user_value % 5 == 0:
        print("Buzz")
    else:
        print(user_value)
else:
    print("Введённое вами число не входит в указанный диапазон")

# Задание 2.1
print("\nЗадание 2.1")
user_value = float(input("Введите число: "))
extent = int(input("Выберите степень от 0 до 7: ")) % 8
print(user_value ** extent)

# Задание 2.2
print("\nЗадание 2.2")
user_value = float(input("Введите число: "))
extent = int(input("Выберите степень от 0 до 7: "))
if extent == 0:
    print(1)
elif extent == 1:
    print(user_value)
elif extent == 2:
    print(user_value ** 2)
elif extent == 3:
    print(user_value ** 3)
elif extent == 4:
    print(user_value ** 4)
elif extent == 5:
    print(user_value ** 5)
elif extent == 6:
    print(user_value ** 6)
elif extent == 7:
    print(user_value ** 7)
else:
    print("Степень не входит в диапазон от 0 до 7")

# Задание 2.3
print("\nЗадание 2.3")
user_value = float(input("Введите число: "))
extent = int(input("Выберите степень от 0 до 7: "))
# конструкция match-case появилась в python 3.10
match extent:
    case 0:
        print(1)
    case 1:
        print(user_value)
    case 2:
        print(user_value ** 2)
    case 3:
        print(user_value ** 3)
    case 4:
        print(user_value ** 4)
    case 5:
        print(user_value ** 5)
    case 6:
        print(user_value ** 6)
    case 7:
        print(user_value ** 7)
    case _:
        print("Степень не входит в диапазон от 0 до 7")

# Задание 3*
print("\nЗадание 3*")
tariffs = {
    "київстар": " 3 грн/пакет 3 хв",
    "vodafone": " 0,60 грн/хв.",
    "lifecell": " 1 грн/ хв"
}

print("""Слава Україні!
Дякуємо що вирішили скористатися нашою послугою.
Ви можете розрахувати вартість дзвінка для таких операторів як  Київстар, Vodafone та lifecell.
""")
from_operator = input("Будь ласка, введіть назву вашого оператора: ").lower()
to_operator = input("Введіть назву оператора на якій ви плануєте дзвонити: ").lower()
if from_operator == to_operator:
    print("В мережі - безкоштовно")
elif from_operator in tariffs and to_operator in tariffs:
    print("Вартість дзвінка" + tariffs[from_operator])
else:
    print("На жаль у нас немає інформації щодо цих операторів")

# Задание 4
print("\nЗадание 4")


def expect_percentage(sale):    # расчитывает процент от продаж
    return {
        sale < 500: sale * 0.03,
        500 <= sale < 1000: sale * 0.05,
        sale >= 1000: sale * 0.08
    }[True]


m1_slevel = int(input("Введите уровень продаж для 1-го менеджера: "))
m2_slevel = int(input("Введите уровень продаж для 2-го менеджера: "))
m3_slevel = int(input("Введите уровень продаж для 3-го менеджера: "))
m1_wages = m2_wages = m3_wages = 200

if m1_slevel > m2_slevel:
    if m1_slevel > m3_slevel:
        m1_wages += 200
    else:
        m3_wages += 200
elif m2_slevel > m3_slevel:
    m2_wages += 200
else:
    m3_wages += 200

print(f"Зарплата 1-го менеджера: {m1_wages + expect_percentage(m1_slevel)}")
print(f"Зарплата 2-го менеджера: {m2_wages + expect_percentage(m2_slevel)}")
print(f"Зарплата 3-го менеджера: {m3_wages + expect_percentage(m3_slevel)}")
