lst = {}
with open('input7.txt') as f:
    for line in f:
        words = line.split()
        val = []
        for i in range(4, len(words) - 3, 4):
            val.append(int(words[i]))
            val.append((words[i + 1], words[i + 2]))
        lst[(words[0], words[1])] = val

root = ('shiny', 'gold')
line = lst[root]
newline = []
summ = 0
oldsumm = 0
flag = True
while flag:
    for i in range(0, len(line), 2):
        summ += int(line[i])
        new = lst[line[i + 1]]
        if new != []:
            for j in range(0, len(new), 2):
                newline.append(new[j] * line[i])
                newline.append(new[j + 1])
    line = newline.copy()
    newline = []
    if oldsumm != summ:
        oldsumm = summ
    else:
        flag = False

print(summ)
