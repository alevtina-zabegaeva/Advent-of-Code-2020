def simple(l):
    spisok = l.split()
    calc = int(spisok[0])
    for i in range(1, len(spisok), 2):
        if spisok[i] == '+':
            calc += int(spisok[i + 1])
        else:
            calc *= int(spisok[i + 1])
    return calc


with open('input18.txt') as f:
    lst = [line.rstrip() for line in f.readlines()]

summa = 0
for lstk in lst:
    flag = True
    while flag:
        flag = False
        j1 = -1
        for j in range(len(lstk) - 1):
            if lstk[j] == '(':
                j1 = j
                flag = True
        j2 = len(lstk)
        if j1 >= 0:
            for j in range(j1, len(lstk)):
                if lstk[j] == ')':
                    j2 = j
                    break
        temp = simple(lstk[j1 + 1: j2])
        if flag:
            lstk = lstk[: j1] + str(temp) + lstk[j2 + 1:]
        else:
            lstk = temp
    summa += lstk

print(summa)
