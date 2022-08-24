# weight = int(input("input weight: "))
# height = int(input("input height: "))
#
# for h in range(height):
#     for w in range(weight):
#         if h == 0 or h == height-1 or w == 0 or w == weight-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# number = int(input("input number: "))
# answer = "Simple"
# for i in range(2, number//2):
#     if number % i == 0:
#         answer = "Not simple"
# print(answer)

# number = int(input("input number: "))
# while number != 0:
#     digit = number % 10
#     number //= 10
#     print(digit, end="-")

# number = int(input("input number: "))
# result = 0
# extent = 0
# while number != 0:
#     digit = number % 10
#     number //= 10
#     result = result + 10 ** extent * digit
#     extent += 1
#     print(digit, end="-")
# print("\n", result)

t_line = 4
t_column = 3

print("    a  b  c  d  e  f  g  h")
print("    -  -  -  -  -  -  -  -")
for line in range(8):
    print(line + 1, end=" |")
    for column in range(8):
        if line == t_line - 1 and column == t_column -1:
            print(" T", end=" ")
        elif line == t_line - 1 or column == t_column - 1:
            print(" X", end=" ")
        else:
            print(" *", end=" ")
    print("|", line + 1)
print("    -  -  -  -  -  -  -  -")
print("    a  b  c  d  e  f  g  h")
