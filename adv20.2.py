import numpy as np
import copy


def get_borders(arr):
    b = ['', '', '', '', '', '', '', '']
    for ii in range(len(arr)):
        b[0] += str(arr[ii, 0])
        b[1] += str(arr[len(arr[0]) - ii - 1, 0])
        b[2] += str(arr[ii, -1])
        b[3] += str(arr[len(arr[0]) - ii - 1, -1])
    for ii in range(len(arr[0])):
        b[4] += str(arr[0, ii])
        b[5] += str(arr[0, len(arr[0]) - ii - 1])
        b[6] += str(arr[-1, ii])
        b[7] += str(arr[-1, len(arr[0]) - ii - 1])
    for bi in range(len(b)):
        b[bi] = int(b[bi], 2)
    return b


N = []
tiles = [np.zeros((10, 10), dtype=int)]
istiles = False
with open('input20test.txt') as f:
    for line in f:
        if line != '\n':
            if istiles:
                for j, li in enumerate(line.rstrip()):
                    if li == '#':
                        tiles[-1][i, j] = 1
                i += 1
            else:
                N.append(int(line[5:-2]))
                tiles.append(np.zeros((10, 10), dtype=int))
                i = 0
                istiles = True
        else:
            istiles = False
tiles.pop(0)
nlen = len(N)

borders = []
tiles_dict = {}
for i, tile in enumerate(tiles):
    bbb = get_borders(tile)
    borders.append(bbb)
    tiles_dict[i] = bbb
borders_dict = {}
for i, border in enumerate(borders):
    for b in border:
        if b in borders_dict:
            borders_dict[b].append(i)
            # borders_dict[b].append(N[i])
        else:
            borders_dict[b] = [i]
            # borders_dict[b] = [N[i]]
border_tiles = []
for key in borders_dict:
    item = borders_dict[key]
    if len(item) == 1:
        border_tiles.append(item[0])
print('borders_dict:', borders_dict)
print('tiles_dict:', tiles_dict)

corners = []
for corner in border_tiles:
    if border_tiles.count(corner) == 4 and corner not in corners:
        corners.append(corner)
print('corners:', corners)

current_tile = corners[0]
puzzle_lb = [[1]]       # change!
puzzle = [[current_tile]]
current_line = 0
flag = True
while flag:
    right_index_current_tile = (2, 3, 0, 1, 6, 7, 4, 5)[puzzle_lb[-1][-1]]
    right_border = tiles_dict[current_tile][right_index_current_tile]
    if len(borders_dict[right_border]) == 1:
        lower_index_first = (6, 4, 7, 5, 2, 0, 3, 1)[puzzle_lb[current_line][0]]
        right_tiles = borders_dict[tiles_dict[puzzle[current_line][0]][lower_index_first]]  # new line!
        if len(right_tiles) == 2:
            if right_tiles[0] == puzzle[current_line][0]:
                right_tile = right_tiles[1]
            else:
                right_tile = right_tiles[0]
            left_index_new_tile = (4, 6, 5, 7, 0, 2, 1, 3)[tiles_dict[right_tile].index(tiles_dict[puzzle[current_line][
                0]][lower_index_first])]
            puzzle.append([right_tile])
            puzzle_lb.append([left_index_new_tile])
            current_line += 1
        else:
            flag = False
    else:
        if borders_dict[right_border][0] == current_tile:
            right_tile = borders_dict[right_border][1]
        else:
            right_tile = borders_dict[right_border][0]
        puzzle[current_line].append(right_tile)
        left_index_right_tile = tiles_dict[right_tile].index(right_border)
        # upper_index = (4, 6, 5, 7, 0, 2, 1, 3)[left_index]
        puzzle_lb[current_line].append(left_index_right_tile)
    current_tile = right_tile

print('tiles = ', puzzle)
print('left borders indexes =', puzzle_lb)

new_tiles = copy.deepcopy(tiles)
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle_lb[i][j] == 1:  # flip horizontal
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][10 - iii - 1][jjj] = tiles[puzzle[i][j]][iii][jjj]
        elif puzzle_lb[i][j] == 2:  # flip vertical
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][iii][10 - jjj - 1] = tiles[puzzle[i][j]][iii][jjj]
        elif puzzle_lb[i][j] == 3:  # flip horizontal and vertical
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][10 - iii - 1][10 - jjj - 1] = tiles[puzzle[i][j]][iii][jjj]
        elif puzzle_lb[i][j] == 4:  # turn clockwise and flip vertical
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][iii][jjj] = tiles[puzzle[i][j]][jjj][iii]
        elif puzzle_lb[i][j] == 5:  # turn counterclockwise
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][iii][jjj] = tiles[puzzle[i][j]][10 - jjj - 1][iii]
        elif puzzle_lb[i][j] == 6:  # turn clockwise
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][iii][jjj] = tiles[puzzle[i][j]][jjj][10 - iii - 1]
        elif puzzle_lb[i][j] == 7:  # turn counterclockwise and flip vertical
            for iii in range(len(tiles[puzzle[i][j]])):
                for jjj in range(len(tiles[puzzle[i][j]][0])):
                    new_tiles[puzzle[i][j]][iii][jjj] = tiles[puzzle[i][j]][10 - jjj - 1][10 - iii - 1]
# pu = [[]*8*len(puzzle)]
pu = [[] for i in range(8*len(puzzle))]
for ii, puzz in enumerate(puzzle):
    for jj, ti in enumerate(puzz):
        for i in range(1, 9):
            pu[i - 1 + ii*8].extend(list(new_tiles[ti][i][1:9]))
big_sum = 0
for pp in pu:
    print(pp)
    big_sum += sum(pp)
print('Big sum =', big_sum)

snake = (((0, 18),  # normal
          (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
          (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)),
         ((0, 1),  # flip vertical
          (1, 19), (1, 14), (1, 13), (1, 8), (1, 7), (1, 2), (1, 1), (1, 0),
          (2, 18), (2, 15), (2, 12), (2, 9), (2, 6), (2, 3)),
         ((2, 18),  # flip horizontal
          (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
          (0, 1), (0, 4), (0, 7), (0, 10), (0, 13), (0, 16)),
         ((2, 1),  # flip vertical and horizontal
          (1, 19), (1, 14), (1, 13), (1, 8), (1, 7), (1, 2), (1, 1), (1, 0),
          (0, 18), (0, 15), (0, 12), (0, 9), (0, 6), (0, 3)),
         ((18, 2),  # rotated clockwise
          (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
          (1, 0), (4, 0), (7, 0), (10, 0), (13, 0), (16, 0)),
         ((18, 0),  # rotated clockwise and flip vertical
          (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
          (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)),
         ((1, 2),  # rotated clockwise and flip horizontal
          (19, 1), (14, 1), (13, 1), (8, 1), (7, 1), (2, 1), (1, 1), (0, 1),
          (18, 0), (15, 0), (12, 0), (9, 0), (6, 0), (3, 0)),
         ((1, 0),  # rotated clockwise and flip horizontal and vertical
          (19, 1), (14, 1), (13, 1), (8, 1), (7, 1), (2, 1), (1, 1), (0, 1),
          (18, 1), (15, 1), (12, 1), (9, 1), (6, 1), (3, 1)))


for snake_counter in range(4):
    found_all = set()
    # pu_temp = copy.deepcopy(pu)
    for i in range(len(pu) - 3):
        for j in range(len(pu[0]) - 20):
            found = set()
            for elem in snake[snake_counter]:
                if pu[i + elem[0]][j + elem[1]] == 0:
                    found = set()
                    break
                else:
                    found.add((i + elem[0], j + elem[1]))
            found_all |= found
    if found_all:
        print(found_all)
        pu_temp = copy.deepcopy(pu)
        for e in found_all:
            pu_temp[e[0]][e[1]] = 8
        for pp in pu_temp:
            print(pp)
        print('Big sum without snakes =', big_sum - len(found_all))
for snake_counter in range(4, 8):
    found_all = set()
    for i in range(len(pu) - 20):
        for j in range(len(pu[0]) - 3):
            found = set()
            for elem in snake[snake_counter]:
                if pu[i + elem[0]][j + elem[1]] == 0:
                    found = set()
                    break
                else:
                    found.add((i + elem[0], j + elem[1]))
            found_all |= found
    if found_all:
        print(found_all)
        pu_temp = copy.deepcopy(pu)
        for e in found_all:
            pu_temp[e[0]][e[1]] = 8
        for pp in pu_temp:
            print(pp)
        print('Big sum without snakes =', big_sum - len(found_all))
