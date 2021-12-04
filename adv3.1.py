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

print(sled(3, 1))
