with open('input14.txt') as f:
    lst = tuple(line.rstrip() for line in f.readlines())

code = []
masks = []
i = -1
for l in lst:
    if l[:4] == 'mask':
        masks.append(l[7:])
        i += 1
        code.append([])
    else:
        equals = l.find('=')
        mem = int(l[4:equals - 2])
        number = int(l[equals + 2:])
        code[i].append((mem, number))
memory = {}
for i, mask in enumerate(masks):
    for m in code[i]:
        number = bin(m[1])[2:]
        number = '0' * (len(masks[i]) -len(number)) + number
        newnumber = ''
        for j in range(len(masks[i])):
            if mask[j] == 'X':
                newnumber += number[j]
            else:
                newnumber += mask[j]
        memory[m[0]] = int(newnumber, 2)
summa = 0
for m in memory:
    summa += memory[m]
# print(lst)
# print(masks)
# print(code)
# print(memory)
print(summa)

