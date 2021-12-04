import numpy as np

words_lst, allergs_lst = [], []
words, allergs = set(), set()
with open('input21.txt') as f:
    for line in f:
        i = line.index('(')
        words_lst.append(line[:i - 1].split(' '))
        words |= set(line[:i - 1].split(' '))
        allergs_lst.append(line.rstrip()[i + 10:-1].split(', '))
        allergs |= set(line.rstrip()[i + 10:-1].split(', '))

n = len(words_lst)  # quantity of lines
array = np.ones((len(words), len(allergs)), dtype=int)
words = list(words)
allergs = list(allergs)
print('words_lst = ', words_lst)
print('allergs_lst =', allergs_lst)
print('words = ', words)
print('allergs = ', allergs)

for i in range(n):
    for ii, word in enumerate(words):
        for jj, allerg in enumerate(allergs):
            if allerg in allergs_lst[i] and word not in words_lst[i]:
                array[ii, jj] = 0

changed = True
while changed:
    changed = False
    for j in range(len(allergs)):
        if sum(array[:, j]) == 1:
            for i in range(len(words)):
                if array[i, j] == 1:
                    for jj in range(len(allergs)):
                        if jj != j:
                            array[i, jj] = 0
        else:
            changed = True

all_allergs = []
for i, word in enumerate(words):
    if sum(array[i, :]) == 1:
        for j, allerg in enumerate(allergs):
            if array[i, j] == 1:
                all_allergs.append(allerg+','+word)
all_allergs.sort()
print(all_allergs)

for element in all_allergs:
    i = element.find(',')
    print(element[i:], end='')
