import string

# Task 1
print("Task 1")
with open("T1_file1.txt") as f1, open("T1_file2.txt") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    i = 0
    while i < len(lines1) and i < len(lines2):
        if not (lines1[i] == lines2[i]):
            print("№: {}\n {:^20}| {} {:^20}| {}".format(i+1, "T1_file1.txt", lines1[i], "T1_file2.txt", lines2[i]))
        i += 1
    while i < len(lines1):
        print("№: {}\n {:^20}| {} {:^20}| ".format(i+1, "T1_file1.txt", lines1[i], "T1_file2.txt", ))
        i += 1
    while i < len(lines2):
        print("№: {}\n {:^20}| {} {:^20}| {}".format(i+1, "T1_file1.txt", " ", "T1_file2.txt", lines2[i]))
        i += 1

# Task 2
print("Task 2")
with open("T2_file.txt") as infile, open("T2_statistics.txt", "w") as outfile:
    text = infile.readlines()
    char_num = 0
    line_num = len(text)
    vowels_num = 0
    consonant_num = 0
    digit_num = 0
    for line in text:
        for s in line:
            char_num += 1
            if s in "aAeEiIoOuUyYаАуУоОыЫэЭяЯюЮёЁиИеЕіІєЄїЇ":
                vowels_num += 1
            if s in "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZбБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩґҐ":
                consonant_num += 1
            if s in string.digits:
                digit_num += 1
    outfile.write(f"Количество символов {char_num}\nКоличество строк {line_num}\nКоличество гласных букв {vowels_num}\n"
                  f"Количество согласных букв {consonant_num}\nКоличество цифр {digit_num}\n")

# Task 3
print("Task 3")
with open("T3_input.txt") as input_file, open("T3_output.txt", "w") as output_file:
    all_lines = input_file.readlines()
    if len(all_lines) > 0:
        all_lines.pop(len(all_lines) - 1)
    output_file.writelines(all_lines)

# Task 4
print("Task 4")
with open("T4_file.txt") as f:
    lines = f.readlines()
    max_len = 0
    for line in lines:
        l_len = len(line)
        if l_len > max_len:
            max_len = l_len
    print("Длина самой длинной строки:", max_len)

# Task 5
print("Task 5")
word = input("Введите слово, которое хотите найти в тексте: ")
with open("T5_file_for_search.txt") as f_search:
    t_search = f_search.read()
    print(f"Слово {word} встречается в тексте {t_search.count(word)} раз")

# Task 6
print("Task 6")
old_word = input("Введите слово, которое хотите заменить: ")
new_word = input("Введите слово, на которое хотите заменить: ")
with open("T6_file.txt") as f, open("T6_file_replace .txt", "w") as f_replace:
    text = f.read()
    text_replace = text.replace(old_word, new_word)
    f_replace.write(text_replace)
