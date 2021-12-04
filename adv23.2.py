def dest_find(d, cs, ps):
    while True:
        if d in ps:
            d -= 1
            if d <= 0:
                d = len(cs)
        else:
            return d


# inpt = '389125467'  # test
inpt = '158937462'
print(inpt)
cups = [0]*len(inpt)

for i in range(len(inpt) - 1):
    cups[int(inpt[i]) - 1] = int(inpt[i + 1])
cups[int(inpt[-1]) - 1] = len(cups) + 1
m = len(cups)
quantity = 1000000
cups.extend(range(len(cups) + 2, quantity + 1))
cups.append(int(inpt[0]))
current_cup = int(inpt[0])

moves = 10000000
for j in range(moves):
    # print('-- move', j + 1, '--')
    # print(cups)
    # print('current_cup =', current_cup)
    pickup = [cups[current_cup - 1]]
    pickup.append(cups[pickup[-1] - 1])
    pickup.append(cups[pickup[-1] - 1])
    # print('pickup =', pickup)
    destination = dest_find(current_cup - 1, cups, pickup)
    # print('destination =', destination)
    cups[current_cup - 1] = cups[pickup[2] - 1]
    cups[pickup[2] - 1] = cups[destination - 1]
    cups[destination - 1] = pickup[0]
    current_cup = cups[current_cup - 1]

# print()
# print('cups =', cups)
print(cups[1 - 1], cups[cups[1 - 1] - 1], cups[1 - 1]*cups[cups[1 - 1] - 1])
