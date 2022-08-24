# def print_en_from_range(start, end):
#     for i in range(start + 1, end):
#         if i % 2 == 0:
#             print(i)
#
#
# print_en_from_range(0, 10)

def draw_square(length, symbol, is_fill=False):
    for i in range(length):
        for j in range(length):
            if not is_fill:
                if i == 0 or i == length - 1 or j == 0 or j == length - 1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")
            else:
                print(symbol, end=" ")
        print()


draw_square(5, "*")


def print_square(len_side, symbol_view, empty):
    for i in range(len_side):
        if i == 0 or i == len_side - 1:
            for j in range(len_side):
                print(symbol_view, end='')
            print()
        else:
            if empty:
                for j in range(len_side):
                    print(symbol_view, end='')
                print()
            else:
                print(symbol_view, end='')
                for j in range(len_side - 2):
                    print(' ', end='')
                print(symbol_view)


print_square(5, 'o', 0)


def fact_rec(f):
    if f == 1:
        return 1
    return f * fact_rec(f - 1)


print(fact_rec(5))
