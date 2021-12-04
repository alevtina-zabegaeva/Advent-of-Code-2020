def round1(d1, d2):
    if len(d1) == 0 or len(d2) == 0:
        return False
    else:
        if d1[0] > d2[0]:
            d1.append(d1.pop(0))
            d1.append(d2.pop(0))
        else:
            d2.append(d2.pop(0))
            d2.append(d1.pop(0))
        return True


flag = True
deck1, deck2 = [], []
with open('input22.txt') as f:
    for line in f:
        if line == '\n':
            flag = False
        else:
            l = line.rstrip()
            if l.isdigit():
                if flag:
                    deck1.append(int(l))
                else:
                    deck2.append(int(l))

flag = True
while flag:
    flag = round1(deck1, deck2)
deck1 = deck1 + deck2
print(deck1)
score = 0
for i in range(1, len(deck1) + 1):
    score += deck1[-i]*i
print(score)
