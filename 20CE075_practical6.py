# 20CE075 PARTH PARMAR
# Practical 6
#  Aim : You are given n words. Some words may repeat. For each word, output its number of occurrences.
#  The output order should correspond with the input order of appearance of the word.
#  See the sample input/output for clarification.
# 

t = int(input())
str1 = ""
str2 = ""
for i in range(t):
    str0 = input()
    length = len(str0)
    mid = int(length / 2)
    if length % 2 == 0:
        str1 = str0[:mid]
        str2 = str0[mid:]
    else:
        str1 = str0[:mid]
        str2 = str0[mid + 1:]
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("YES")
    else:
        print("NO")
