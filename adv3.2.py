def sled(r, d):
    j, counter = 0, 0
    for i in range(0, len(wood), d):
        if wood[i][j] == '#':
            counter += 1
        j = (j + r) % len(wood[i])
    return counter


wood = []
with open('input3.txt') as f:
    for line in f:
        wood.append(line.rstrip())

paths = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
res = 1
for p in paths:
    res *= sled(*p)
print(res)
