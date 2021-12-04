counter: int = 0
with open('input2.txt') as f:
    for line in f:
        ind1 = line.find('-')
        ind2 = line.find(' ')
        num1 = int(line[:ind1])
        num2 = int(line[ind1 + 1:ind2])
        s1 = line[ind2 + 3 + num1]
        s2 = line[ind2 + 3 + num2]
        if int(s1 == line[ind2 + 1]) ^ int(s2 == line[ind2 + 1]):
            counter += 1

print(counter)
