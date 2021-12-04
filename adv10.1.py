with open('input10.txt') as f:
    lst = list(map(int, f.read().split()))

j = 0
dif = []
lst.sort()

for i in range(len(lst)):
    dif.append(lst[i] - j)
    j = lst[i]

print(dif.count(1) * (dif.count(3) + 1))
