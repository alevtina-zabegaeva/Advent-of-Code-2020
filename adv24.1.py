def take_direction(l):
    direction = l.pop(0)
    if direction == 's' or direction == 'n':
        direction += l.pop(0)
    return direction


with open('input24.txt') as f:
    lst = [list(line.rstrip()) for line in f.readlines()]

tiles = set()
for i in range(len(lst)):
    current = [0, 0]
    while len(lst[i]) != 0:
        d = take_direction(lst[i])
        if d == 'e':
            current[1] += 1
        elif d == 'w':
            current[1] -= 1
        elif d == 'se':
            if current[0] % 2 == 1:
                current[1] += 1
            current[0] += 1
        elif d == 'sw':
            if current[0] % 2 == 0:
                current[1] -= 1
            current[0] += 1
        elif d == 'ne':
            if current[0] % 2 == 1:
                current[1] += 1
            current[0] -= 1
        elif d == 'nw':
            if current[0] % 2 == 0:
                current[1] -= 1
            current[0] -= 1
    current = tuple(current)
    if current in tiles:
        tiles.remove(current)
    else:
        tiles.add(current)

print(tiles)
print(len(tiles))
