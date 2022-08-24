from random import randint


# Task 1
print("\nTask 1")


def qsort(some_list, f_index, l_index):
    i = f_index
    j = l_index
    # pivot element in the middle
    pivot_elem = some_list[(l_index + f_index) // 2]
    while i <= j:
        while some_list[i] < pivot_elem:
            i += 1

        while some_list[j] > pivot_elem:
            j -= 1

        if i <= j:  # swap
            some_list[i], some_list[j] = some_list[j], some_list[i]
            i += 1
            j -= 1
    if f_index < j:  # sort left part
        qsort(some_list, f_index, j)
    if i < l_index:  # sort right part
        qsort(some_list, i, l_index)


def reverse_list(some_list, f_index, l_index):
    while f_index < l_index:
        some_list[f_index], some_list[l_index] = some_list[l_index], some_list[f_index]
        f_index += 1
        l_index -= 1


def arithmetical_mean(lis):
    return sum(lis) / len(lis)


li = [randint(-20, 20) for i in range(15)]
print("Input li:", li)

first_index = len(li) // 3 + 1 if len(li) % 3 == 2 else len(li) // 3
print("first index: ", first_index)
print("mean: ", arithmetical_mean(li))

if arithmetical_mean(li) > 0:
    qsort(li, 0, first_index * 2 - 1)
    reverse_list(li, first_index * 2, len(li) - 1)

else:
    qsort(li, 0, first_index - 1)
    reverse_list(li, first_index, len(li) - 1)

print("Output li:", li)

# Task 2
print("\nTask 2")

grade_list = []
for i in range(10):
    try:
        grade = int(input(f"Enter {i + 1} grade: "))
        if not (0 < grade < 13):
            raise ValueError
        grade_list.append(grade)
    except ValueError:
        grade_list.append(1)
print("""
0 - program shutdown
1 - display a list of grades
2 - retaking the exam
3 - learn about the scholarship
4 - ascending grade list
5 - descending list of grades
""")

while True:
    command = input("Enter a number from 0 to 5: ")
    if command == "0":
        print("\tGoodbye!")
        break
    elif command == "1":
        print("\t", grade_list)
    elif command == "2":
        while True:
            try:
                index = int(input("\tEnter the exam index from 1 to 10: "))
                if not (0 < index < 11):
                    raise ValueError
                break
            except ValueError:
                print("\tWrong index")
        try:
            grade = int(input(f"\tInput {index} grade: "))
            grade_list[index - 1] = grade
        except ValueError:
            grade_list[index - 1] = 1

    elif command == "3":
        gpa = arithmetical_mean(grade_list)
        print(
            f"\tYou get a scholarship, your GPA is {gpa}" if gpa >= 10.7 else f"\tYou DON'T receive a scholarship, your"
                                                                              f" GPA is {gpa}")
    elif command == "4":
        print("\t", sorted(grade_list))
    elif command == "5":
        print("\t", sorted(grade_list, reverse=True))
    else:
        print("Unknown command")

# Task 3
print("\nTask 3")

random_list = [randint(0, 20) for i in range(15)]

print("random list: ", random_list)


def smart_bubble_sort(some_list, reverse=False):
    for i in range(len(some_list) - 1):
        num_of_permutations = 0
        for j in range(len(some_list) - i - 1):
            if some_list[j] < some_list[j + 1] if reverse else some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
                num_of_permutations += 1
        # print("num_of_permutations: ", num_of_permutations, "i: ", i)
        if num_of_permutations == 0:
            break


smart_bubble_sort(random_list)
print("sorted list: ", random_list)
