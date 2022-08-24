# Задание 1
print("# Задание 1")
num1 = int(input("Введите первую цифру: "))
num2 = int(input("Введите вторую цифру: "))
num3 = int(input("Введите третью цифру: "))
mix_num = int(str(num1) + str(num2) + str(num3))
print(mix_num)

# Задание 2
print("\n# Задание 2")
num_4_digit = int(input("Введите четырехзначное число: "))

mp_digit = num_4_digit // 1000
temp = num_4_digit % 1000

mp_digit *= temp // 100
temp = temp % 100

mp_digit *= temp // 10

mp_digit *= temp % 10

print(mp_digit)

# Задание 3
print("\n# Задание 3")
meter = float(input("Введите количество метров: "))
print(f"{meter} м = {meter*100} см")
print(f"{meter} м = {meter*10} дм")
print(f"{meter} м = {meter*1000} мм")
print(f"{meter} м = {meter*0.000621371} миля")

# Задание 4
print("\n# Задание 4")
t_base = float(input("Введите длину основания треугольника: "))
t_height = float(input("Введите длину высоты треугольника, проведенной к основанию: "))
print(f"Площадь треугольника: ", 0.5*t_base*t_height)

# Задание 5
print("\n# Задание 5")
num_4_digit = int(input("Введите четырехзначное число: "))

inverted_num = (num_4_digit % 10)*1000
temp = num_4_digit // 10

inverted_num += (temp % 10)*100
temp = temp // 10

inverted_num += (temp % 10)*10

inverted_num += (temp // 10)

print(inverted_num)
