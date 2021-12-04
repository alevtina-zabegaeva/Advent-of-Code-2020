def sosedi(iz, jz, karta):
    # 0: left, 1: right, 2: up, 3: down, 4: leftup, 5: leftdown, 6: rightup, 7: rightdown
    Nachbars = []
    vektors = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
    see = list(vektors)
    for num, vektor in enumerate(vektors):
        while True:
            if karta[iz + see[num][0]][jz + see[num][1]] == '.':
                nexti, nextj = see[num][0] + vektor[0], see[num][1] + vektor[1]
                if 0 <= iz + nexti < len(karta) and 0 <= jz + nextj < len(karta[iz]):
                    see[num] = (nexti, nextj)
                else:
                    break
            else:
                break
        Nachbars.append(karta[iz + see[num][0]][jz + see[num][1]])
    return Nachbars


with open('input11.txt') as f:
    lst = ['.' + line.strip('\n') + '.' for line in f.readlines()]
lst.insert(0, '.' * len(lst[-1]))
lst.append('.' * len(lst[-1]))

oldlst = lst.copy()
change_flag = True
while change_flag:
    change_flag = False
    newlst = ['.' * len(lst[-1])]
    for i in range(1, len(lst) - 1):
        newline = '.'
        for j in range(1, len(lst[i]) - 1):
            sym = oldlst[i][j]
            newline += sym
            if sym == 'L':
                if sosedi(i, j, oldlst).count('#') == 0:
                    newline = newline[:-1] + '#'
                    change_flag = True
            elif sym == '#':
                if sosedi(i, j, oldlst).count('#') >= 5:
                    newline = newline[:-1] + 'L'
                    change_flag = True
        newlst.append(newline + '.')
    newlst.append('.' * len(lst[-1]))
    oldlst = newlst.copy()

counter = 0
for line in newlst:
    # print(line)
    counter += line.count('#')
print(counter)
