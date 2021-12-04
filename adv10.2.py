def check_num(n, c):
    if c == 2:
        n *= 2
    elif c == 3:
        n *= 4
    elif c == 4:
        n *= 7
    return n


with open('input10.txt') as f:
    lst = list(map(int, f.read().split()))

j = 0
dif = []
lst.sort()
counter = 0
num = 1
for i in range(len(lst)):
    dif.append(lst[i] - j)
    j = lst[i]
    if dif[-1] == 1:
        counter += 1
    else:
        num = check_num(num, counter)
        counter = 0
dif.append(3)
num = check_num(num, counter)

# print(dif)
print(num)
