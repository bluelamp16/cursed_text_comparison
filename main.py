def compare(text1, text2):
    n, m = len(text1), len(text2)
    if n > m:
        text1, text2 = text2, text1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if text1[j - 1] != text2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]

name1, name2= input().split()

open_1 = open(name1)
open_2 = open(name2)

txt1 = open_1.read().replace("\n", " ")
txt2 = open_2.read().replace("\n", " ")

print(compare(txt1, txt2)/len(txt1))
