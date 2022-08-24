import random

list1 = [random.randint(0, 10) for i in range(0, 5)]
list2 = [random.randint(0, 10) for i in range(0, 5)]
print("list1\t\t", list1)
print("list2\t\t", list2)

# третий список, содержащий элементы обоих списков
list3all = list1 + list2
print("list3all\t", list3all)

# третий список, содержащий элементы обоих списков без повторений
list3wr = list3all.copy()
for i in list3wr:
    if list3wr.count(i) > 1:
        list3wr.remove(i)
print(f"list3wr\t\t", list3wr)

# третий список, содержащий элементы общие для двух списков
list3jnt = []
for i in list1:
    if i in list2 and not (i in list3jnt):
        list3jnt.append(i)
print(f"list3jnt\t", list3jnt)

# третий список, содержащий только уникальные элементы каждого из списков
list3unq = []
for i in list1:
    if not (i in list2) and not (i in list3unq) and list1.count(i) == 1:
        list3unq.append(i)
for i in list2:
    if not (i in list1) and not (i in list3unq) and list2.count(i) == 1:
        list3unq.append(i)
print(f"list3unq\t", list3unq)

# третий список, содержащий только минимальное и максимальное значение каждого из списков
list3mm = [min(list1), max(list1), min(list2), max(list2)]
print(f"list3mm\t\t", list3mm)
