tickets = set()
with open('input5.txt') as f:
    for line in f:
        tickets.add(line.rstrip())

maximumID = 0
for ticket in tickets:
    num = ticket.replace('F', '0').replace('L', '0').replace('R', '1').replace('B', '1')
    ID = int(num, 2)
    maximumID = max(maximumID, ID)

print(maximumID)
