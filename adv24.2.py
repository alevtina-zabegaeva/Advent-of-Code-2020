def take_direction(li):
    direction = li.pop(0)
    if direction == 's' or direction == 'n':
        direction += li.pop(0)
    return direction


def sosedi(t):
    s = [(t[0], t[1] + 1), (t[0], t[1] - 1), (t[0] + 1, t[1]), (t[0] - 1, t[1])]
    if t[0] % 2 == 0:
        s.extend([(t[0] + 1, t[1] - 1), (t[0] - 1, t[1] - 1)])
    else:
        s.extend([(t[0] + 1, t[1] + 1), (t[0] - 1, t[1] + 1)])
    return s


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

for j in range(100):
    tiles_new = tiles.copy()
    for tile in tiles:
        sosedi_black = sosedi(tile)
        counter_black = 0
        for s_black in sosedi_black:
            if s_black in tiles:
                counter_black += 1
            else:
                sosedi_white = sosedi(s_black)
                counter_white = 0
                for s_white in sosedi_white:
                    if s_white in tiles:
                        counter_white += 1
                if counter_white == 2:
                    tiles_new.add(s_black)
        if counter_black == 0 or counter_black > 2:
            tiles_new.remove(tile)
    tiles = tiles_new
print(j+1, len(tiles))
