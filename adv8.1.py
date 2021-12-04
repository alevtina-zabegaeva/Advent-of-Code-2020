lst = []
with open('input8.txt') as f:
    for line in f:
        words = line.split()
        lst.append((words[0], int(words[1])))

print(lst)
accu = 0
i = 0
used_ind = set()
used_ind.add(0)
while True:
    print(i, accu, lst[i])
    if lst[i][0] == 'acc':
        accu += lst[i][1]
        i += 1
    elif lst[i][0] == 'nop':
        i += 1
    else:
        i += lst[i][1]
    if i in used_ind:
        break
    else:
        used_ind.add(i)

print(accu)
