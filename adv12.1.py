with open('input12.txt') as f:
    lst = tuple((line.rstrip()[0], int(line.rstrip()[1:])) for line in f.readlines())

#             east,   south,    west,   north
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
turn = {'R': 1, 'L': -1}
move = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
current_direction = 0
coordinate = [0, 0]
for step in lst:
    if step[0] in move:
        coordinate[0] += move[step[0]][0] * step[1]
        coordinate[1] += move[step[0]][1] * step[1]
    elif step[0] in turn:
        current_direction = (current_direction + turn[step[0]] * step[1] // 90) % 4
    else:
        coordinate[0] += directions[current_direction][0] * step[1]
        coordinate[1] += directions[current_direction][1] * step[1]
    #print(coordinate)

print(abs(coordinate[0]) + abs(coordinate[1]))
