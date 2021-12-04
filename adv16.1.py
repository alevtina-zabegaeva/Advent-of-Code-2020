import re


def check_number(n):
    for border in borders:
        for i in range(0, len(border), 2):
            if int(border[i]) <= n <= int(border[i + 1]):
                return True
    return False


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

summ = 0
for ticket in tickets:
    for t in ticket:
        if not check_number(int(t)):
            summ += int(t)

print(summ)
# print(borders)
# print(entities)
# print(myticket)
# print(tickets)
