import re


def check_number(n):
    indexes = set()
    for k, border in enumerate(borders):
        if int(border[0]) <= n <= int(border[1]) or int(border[2]) <= n <= int(border[3]):
            indexes.add(k)
    return indexes


borders = []
entities = []
tickets = []
i = 0
with open('input16.txt') as f:
    for line in f:
        if line != '\n':
            if i == 0:
                borders.append(re.findall(r'\d+', line))
                entities.append(line.split(':')[0])
            elif i == 1:
                myticket = line.rstrip().split(',')
            else:
                tickets.append(line.rstrip().split(','))
        else:
            i += 1
tickets.pop(0)

index_del = []
all_indexes = [[] for i in range(len(tickets))]
for i in range(len(tickets)):
    for j, t in enumerate(tickets[i]):
        checked_index = check_number(int(t))
        if not checked_index:
            index_del.append(i)
        else:
            all_indexes[i].append(checked_index)
index_del.reverse()
for i in index_del:
    tickets.pop(i)
    all_indexes.pop(i)

checked = all_indexes[0].copy()
for ticket in all_indexes:
    for j, t in enumerate(ticket):
        checked[j] = checked[j] & t

set_of_found = set()
flag = True
while flag:
    flag = False
    for i, c in enumerate(checked):
        if len(c) == 1:
            set_of_found |= c
        else:
            c -= set_of_found
            flag = True

product = 1
for i, item in enumerate(checked):
    if entities[item.pop()][:10] == 'departure ':
        product *= int(myticket[i])

print(product)
