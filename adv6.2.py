lst = [set('abcdefghijklmnopqrstuvwxyz')]
i = 0
with open('input6.txt') as f:
    for line in f:
        if line == '\n':
            i += 1
            lst.append(set('abcdefghijklmnopqrstuvwxyz'))
        else:
            lst[i] = lst[i].intersection(set(line.rstrip()))

l = 0
for s in lst:
    l += len(s)
print(l)
