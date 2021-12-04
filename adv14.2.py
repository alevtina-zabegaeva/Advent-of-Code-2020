import itertools

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
        m_bin = bin(m[0])[2:]
        m_bin = '0' * (len(masks[i]) - len(m_bin)) + m_bin
        for j in range(len(masks[i])):
            if mask[j] == '1' or mask[j] == 'X':
                m_bin = m_bin[:j] + mask[j] + m_bin[j + 1:]
        deg = m_bin.count('X')
        variants = itertools.product(('0', '1'), repeat=deg)
        for var in variants:
            m_bin_all = m_bin
            for k in range(deg):
                m_bin_all = m_bin_all.replace('X', var[k], 1)
            memory[int(m_bin_all, 2)] = int(m[1])
summa = 0
for m in memory:
    summa += memory[m]
print(summa)
