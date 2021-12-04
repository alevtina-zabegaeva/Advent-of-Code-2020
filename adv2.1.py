counter: int = 0
with open('input2.txt') as f:
    for line in f:
        ind1 = line.find('-')
        ind2 = line.find(' ')
        num1 = int(line[:ind1])
        num2 = int(line[ind1 + 1:ind2])
        if num1 <= (line.count(line[ind2 + 1]) - 1) <= num2:
            counter += 1

print(counter)
