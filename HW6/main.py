import re

# Task 1
# istr = input("Enter the string: ")
# istr = istr.lower()
# istr = re.sub(" ", "", istr)
# rev_str = istr[::-1]
# print(istr)
# print(rev_str)
# print("Your string is a palindrome" if istr == rev_str else "Your string is not a palindrome")
# # кок
# # А роза упала на лапу Азора
# # доход
# # А буду я у дуба

# Task 2
text = input("Enter text: ")
reswordslist = []
print("To stop, enter !")
while True:
    w = input("Enter the reserved word: ")
    if w != "!":
        reswordslist.append(w)
    else:
        break
print(reswordslist)

for w in reswordslist:
    text = text.replace(w, w.upper())
print(text)

# Task 3
# text = input("Enter text: ")
# amount = 0
# for i in range(len(text)):
#     if text[i] == "!" and (i + 2 >= len(text) or text[i + 2].isupper() or text[i + 2] == "\""):
#         amount += 1
#         # print("! ", i)
#     if text[i] == "?" and (i + 2 >= len(text) or text[i + 2].isupper() or text[i + 2] == "\""):
#         amount += 1
#         # print("? ", i)
#     if text[i] == "." and (i + 2 >= len(text) or text[i + 2].isupper() or text[i + 2] == "\""):
#         amount += 1
#         # print(". ", i)
#     if text[i] == "..." and (i + 2 >= len(text) or text[i + 2].isupper() or text[i + 2] == "\""):
#         amount += 1
#         # print("... ", i)
# print(amount, "sentences in the text")
