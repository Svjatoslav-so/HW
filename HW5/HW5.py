# часть 4
#   Задание 1
print("Часть 4")
print("\tЗадание 1")

r_start = int(input("Enter start of range: "))
r_end = int(input("Enter end of range: "))

if r_start <= 1:
    r_start = 2
if r_end > r_start:
    for n in range(r_start, r_end + 1):
        is_prime = True
        for d in range(2, n // 2 + 1):
            # print(f" {n} {d} {n % d}")
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")
    print()

#   Задание 2
print("\n\tЗадание 2")

for i in range(1, 11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}", end="\t\t")
    print()

#   Задание 2
print("\n\tЗадание 3")

r_start = int(input("Enter start of range: "))
r_end = int(input("Enter end of range: "))
for i in range(r_start, r_end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t\t")
    print()

# часть 5
#   Задание 1
print("\nЧасть 5")
print("\tЗадание 1")

side_length = 11
print("Enter 0 to exit")
while True:
    choice = int(input("Enter a number from 1 to 10: "))
    if choice == 1:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w < h:
                    print("   ", end="")
                else:
                    print(" * ", end="")
            print()

    elif choice == 2:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w > h:
                    print("   ", end="")
                else:
                    print(" * ", end="")
            print()
    elif choice == 3:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if h <= w <= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 4:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if h >= w >= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 5:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if h >= w >= side_length + 1 - h or h <= w <= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 6:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if h > w > side_length + 1 - h or h < w < side_length + 1 - h:
                    print("   ", end="")
                else:
                    print(" * ", end="")
            print()
    elif choice == 7:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w <= h and w <= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 8:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w >= h and w >= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 9:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w <= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 10:
        for h in range(1, side_length + 1):
            for w in range(1, side_length + 1):
                if w >= side_length + 1 - h:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    elif choice == 0:
        print("shutdown")
        break
    else:
        print("wrong command")
