from random import randint

li = [randint(1, 20) for i in range(10)]
print(li)


# Sort
# li.sort()
def bubble_sort(lis):
    for j in range(len(lis) - 1):
        for i in range(len(lis) - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]


def select_sort(lis):
    start = 0
    for i in range(start, len(lis)):
        index_min = lis[start:].index(min(lis[start:]))
        print(lis[start:])
        print(index_min)
        index_min += start
        lis[start], lis[index_min] = lis[index_min], lis[start]
        print(lis)
        start += 1


# bubble_sort(li)
# select_sort(li)
# print(li)

# Search

def liner_search(lis, value):
    for i in lis:
        if i == value:
            return lis.index(i)
    return -1


print(liner_search(li, 10))


def ShellSort(myList):
    subListN = len(myList) // 2
    step = 1
    while subListN > 0:
        for startInd in range(subListN):
            InsertionSort(myList, startInd, subListN)
        print("Interval={}. After step {}: {}".format(subListN, step, myList))
        subListN = subListN // 2


def InsertionSort(myList, startInd, gapValue):
    print("start")
    for i in range(startInd + gapValue, len(myList), gapValue):
        currentElem = myList[i]
        currentInd = i
        print("CurrentInd", currentInd)
        while currentInd >= gapValue and myList[currentInd - gapValue] > currentElem:
            myList[currentInd] = myList[currentInd - gapValue]
            currentInd = currentInd - gapValue
            myList[currentInd] = currentElem


numbers = [33, 31, 40, 8, 12, 17, 25, 42]
print("Original list: {}".format(numbers))
ShellSort(numbers)
print("Sorted list: {}".format(numbers))
