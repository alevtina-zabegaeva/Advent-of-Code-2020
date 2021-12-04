i = 0
lst = [{}]
with open('input4.txt') as f:
    for line in f:
        if line == '\n':
            i += 1
            lst.append({})
        else:
            for field in line.rstrip().split(' '):
                lst[i][field[:3]] = field[4:]

counter = 0
for elem in lst:
    if len(elem) == 8 or len(elem) == 7 and elem.get('cid') is None:
        counter += 1

print(counter)
