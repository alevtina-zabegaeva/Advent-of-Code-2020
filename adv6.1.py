lst = [set()]
i = 0
with open('input6.txt') as f:
    for line in f:
        if line == '\n':
            i += 1
            lst.append(set())
        else:
            lst[i] = lst[i].union(set(line.rstrip()))

l = 0
for s in lst:
    l += len(s)
print(l)
