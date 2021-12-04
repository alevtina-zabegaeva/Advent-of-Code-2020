def sosedi(iz, jz, karta):
    return [karta[iz][jz-1], karta[iz][jz+1], karta[iz-1][jz], karta[iz+1][jz],
            karta[iz-1][jz-1], karta[iz-1][jz+1], karta[iz+1][jz-1], karta[iz+1][jz+1]]


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
                if sosedi(i, j, oldlst).count('#') >= 4:
                    newline = newline[:-1] + 'L'
                    change_flag = True
        newlst.append(newline + '.')
    newlst.append('.' * len(lst[-1]))
    oldlst = newlst.copy()

counter = 0
for line in newlst:
    print(line)
    counter += line.count('#')
print(counter)
