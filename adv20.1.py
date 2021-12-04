import numpy as np


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
with open('input20.txt') as f:
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

borders = []
for tile in tiles:
    borders.append(get_borders(tile))
borders_dict = {}
for i, border in enumerate(borders):
    for b in border:
        if b in borders_dict:
            borders_dict[b].append(N[i])
        else:
            borders_dict[b] = [N[i]]
corners_all = []
for key in borders_dict:
    item = borders_dict[key]
    if len(item) == 1:
        corners_all.append(item[0])
corners = set()
for corner in corners_all:
    if corners_all.count(corner) == 4:
        corners.add(corner)
p = 1
for corner in corners:
    p *= corner
print(p)
