def dest_find(d, cs):
    while True:
        if d not in cs:
            d -= 1
            if d <= 0:
                d = max(cs)
        else:
            return d


def insert_pickup(cs, ps, di):
    di += 1
    for i in (2, 1, 0):
        cs.insert(di, ps[i])
    return


# inpt = '389125467'  # test
inpt = '158937462'

cups = list(int(i) for i in inpt)

moves = 100
for j in range(moves):
    print('-- move', j + 1, '--')
    print('cups =', cups)
    current_cup = cups[0]
    pickup = cups[1:4]
    print('pickup =', pickup)
    cups = cups[4:]
    cups.insert(0, current_cup)
    destination = dest_find(current_cup - 1, cups)
    print('destination =', destination)
    print()
    d_ind = cups.index(destination)
    insert_pickup(cups, pickup, d_ind)
    cups.pop(0)
    cups.append(current_cup)

print('cups =', cups)
ind1 = cups.index(1)
for i in range(ind1 + 1, len(cups)):
    print(cups[i], end='')
for i in range(0, ind1):
    print(cups[i], end='')
