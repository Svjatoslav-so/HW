# c_line = 4
# c_column = 3

for c_line in range(1, 9):
    for c_column in range(1, 9):

        print(f"ЛАДЬЯ [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if ln == c_line - 1 and clmn == c_column - 1:
                    print(" T", end=" ")
                elif ln == c_line - 1 or clmn == c_column - 1:
                    print(" X", end=" ")
                # для рисования черных клеток
                # elif ln % 2 == 0 and clmn % 2 != 0 or ln % 2 != 0 and clmn % 2 == 0:
                #     print("▓▓", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"СЛОН [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if ln == c_line - 1 and clmn == c_column - 1:
                    print(" S", end=" ")
                elif clmn == ln + c_column - c_line or clmn + ln == c_column - 1 + c_line - 1:
                    print(" X", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"КОРОЛЕВА [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if ln == c_line - 1 and clmn == c_column - 1:
                    print(" Q", end=" ")
                elif (ln == c_line - 1 or clmn == c_column - 1) \
                        or (clmn == ln + c_column - c_line or clmn + ln == c_column - 1 + c_line - 1):
                    print(" X", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"КОНЬ [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if ln == c_line - 1 and clmn == c_column - 1:
                    print(" H", end=" ")
                elif ln == c_line - 1 - 2 and (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) \
                        or ln == c_line - 1 + 2 and (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) \
                        or clmn == c_column - 1 + 2 and (ln == c_line - 1 + 1 or ln == c_line - 1 - 1) \
                        or clmn == c_column - 1 - 2 and (ln == c_line - 1 + 1 or ln == c_line - 1 - 1):
                    print(" X", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"КОРОЛЬ [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if ln == c_line - 1 and clmn == c_column - 1:
                    print(" K", end=" ")
                elif ln == c_line - 1 and (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) \
                        or clmn == c_column - 1 and (ln == c_line - 1 + 1 or ln == c_line - 1 - 1) \
                        or ln == c_line - 1 + 1 and (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) \
                        or ln == c_line - 1 - 1 and (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1):
                    print(" X", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"ПЕШКА (идет снизу) [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if c_line != 8:
                    if ln == c_line - 1 and clmn == c_column - 1:
                        print(" P", end=" ")
                    elif c_line - 1 == 6 and c_line - 1 >= ln >= c_line - 1 - 2 and clmn == c_column - 1 \
                            or clmn == c_column - 1 and ln == c_line - 1 - 1:
                        print(" Y", end=" ")
                    elif (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) and ln == c_line - 1 - 1:
                        print(" X", end=" ")
                    else:
                        print("  ", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print(f"ПЕШКА (идет сверху) [{c_line}, {c_column}]")
        print("    a  b  c  d  e  f  g  h")
        print("    -  -  -  -  -  -  -  -")
        for ln in range(8):
            print(ln + 1, end=" |")
            for clmn in range(8):
                if c_line != 1:
                    if ln == c_line - 1 and clmn == c_column - 1:
                        print(" P", end=" ")
                    elif c_line - 1 == 1 and c_line - 1 <= ln <= c_line - 1 + 2 and clmn == c_column - 1 \
                            or clmn == c_column - 1 and ln == c_line - 1 + 1:
                        print(" Y", end=" ")
                    elif (clmn == c_column - 1 + 1 or clmn == c_column - 1 - 1) and ln == c_line - 1 + 1:
                        print(" X", end=" ")
                    else:
                        print("  ", end=" ")
                else:
                    print("  ", end=" ")
            print("|", ln + 1)
        print("    -  -  -  -  -  -  -  -")
        print("    a  b  c  d  e  f  g  h")

        print("#################################################")
