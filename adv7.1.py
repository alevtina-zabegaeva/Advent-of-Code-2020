lst = {}
with open('input7.txt') as f:
    for line in f:
        words = line.split()
        val = []
        for i in range(4, len(words) - 3, 4):
            val.append(int(words[i]))
            val.append((words[i + 1], words[i + 2]))
        lst[(words[0], words[1])] = val

goal = ('shiny', 'gold')

goals = set()
goals.add(goal)
newgoals = set()
allgoals = set()
while len(goals) != 0:
    for element in lst:
        for go in goals:
            if go in lst[element]:
                newgoals.add(element)
    allgoals = allgoals.union(newgoals)
    goals = newgoals
    newgoals = set()

print(len(allgoals))
