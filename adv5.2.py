tickets = set()
with open('input5.txt') as f:
    for line in f:
        tickets.add(line.rstrip())

IDs = []
for ticket in tickets:
    num = ticket.replace('F', '0').replace('L', '0').replace('R', '1').replace('B', '1')
    IDs.append(int(num, 2))

IDs.sort()
for i in range(1, len(IDs) - 1):
    if IDs[i + 1] - IDs[i] == 2:
        print(IDs[i] + 1)
