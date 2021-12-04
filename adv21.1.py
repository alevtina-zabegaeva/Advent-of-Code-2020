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
print(array)

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
print(array)

not_allergs = set()
for i, word in enumerate(words):
    if sum(array[i, :]) == 0:
        not_allergs.add(word)
print(not_allergs)

counter = 0
for word_lst in words_lst:
    for w in word_lst:
        if w in not_allergs:
            counter += 1
print(counter)