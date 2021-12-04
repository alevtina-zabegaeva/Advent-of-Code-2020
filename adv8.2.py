def run_code(code):
    flag = False
    accu, i = 0, 0
    used_ind = set()
    used_ind.add(0)
    while i != len(lst):
        if code[i][0] == 'acc':
            accu += code[i][1]
            i += 1
        elif code[i][0] == 'nop':
            i += 1
        else:
            i += code[i][1]
        if i in used_ind:
            break
        else:
            used_ind.add(i)
    if i == len(code):
        flag = True
    return accu, flag


lst = []
with open('input8.txt') as f:
    for line in f:
        words = line.split()
        lst.append((words[0], int(words[1])))

for j in range(len(lst)):
    new_lst = lst.copy()
    if lst[j][0] == 'nop':
        new_lst[j] = ('jmp', lst[j][1])
    elif lst[j][0] == 'jmp':
        new_lst[j] = ('nop', lst[j][1])
    a, if_end = run_code(new_lst)
    if if_end == True:
        print(a)
        break
