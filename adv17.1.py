import numpy as np


def sosedi(x_s, k_s, i_s, j_s):
    summ = - x_s[k_s, i_s, j_s]
    for k_sos in (k_s - 1, k_s, k_s + 1):
        for i_sos in (i_s - 1, i_s, i_s + 1):
            for j_sos in (j_s - 1, j_s, j_s + 1):
                summ += x_s[k_sos, i_sos, j_sos]
    return summ


with open('input17.txt') as f:
    lst = tuple(line.rstrip() for line in f.readlines())

steps = 6
x = np.zeros((1 + steps * 2+2, len(lst) + steps * 2+2, len(lst[0]) + steps * 2+2), dtype=int)

for i, line in enumerate(lst):
    for j, l in enumerate(line):
        if l == '#':
            x[steps, steps + i, steps + j] = 1
new_x = x.copy()
old_x = x.copy()

for counter in range(steps):
    for k in range(0, len(x) - 1):
        for i in range(0, len(x[0]) - 1):
            for j in range(0, len(x[0][0]) - 1):
                s = sosedi(old_x, k, i, j)
                if old_x[k, i, j] == 1 and s != 2 and s != 3:
                    new_x[k, i, j] = 0
                elif old_x[k, i, j] == 0 and s == 3:
                    new_x[k, i, j] = 1
    old_x = new_x.copy()

print(new_x.sum())
