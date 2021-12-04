import math

with open('input12.txt') as f:
    lst = tuple((line.rstrip()[0], int(line.rstrip()[1:])) for line in f.readlines())

#             east,   south,    west,   north
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
turn = {'R': -1, 'L': 1}
move = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
coordinate = [0, 0]
waypoint = [10, 1]
for step in lst:
    if step[0] in move:
        waypoint[0] += move[step[0]][0] * step[1]
        waypoint[1] += move[step[0]][1] * step[1]
    elif step[0] in turn:
        next_e = round(math.cos(turn[step[0]] * math.radians(step[1])) * waypoint[0] -
                     math.sin(turn[step[0]] * math.radians(step[1])) * waypoint[1])
        next_n = round(math.sin(turn[step[0]] * math.radians(step[1])) * waypoint[0] +
                     math.cos(turn[step[0]] * math.radians(step[1])) * waypoint[1])
        waypoint[0] = next_e
        waypoint[1] = next_n
    else:
        coordinate[0] += waypoint[0] * step[1]
        coordinate[1] += waypoint[1] * step[1]
    # print(coordinate, waypoint)

print(abs(coordinate[0]) + abs(coordinate[1]))
