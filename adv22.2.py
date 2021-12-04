def round1(d1, d2):
    if d1[0] > d2[0]:
        d1.append(d1.pop(0))
        d1.append(d2.pop(0))
    else:
        d2.append(d2.pop(0))
        d2.append(d1.pop(0))


def whole_game(de1, de2):
    check = set()
    while True:
        if (tuple(de1), tuple(de2)) in check:
            return 1
        else:
            check.add((tuple(de1), tuple(de2)))
        if len(de1) == 0:
            return 2
        elif len(de2) == 0:
            return 1
        if de1[0] < len(de1) and de2[0] < len(de2):
            # print(de1, de2)
            if whole_game(de1[1:de1[0] + 1], de2[1:de2[0] + 1]) == 1:
                de1.append(de1.pop(0))
                de1.append(de2.pop(0))
            else:
                de2.append(de2.pop(0))
                de2.append(de1.pop(0))
        else:
            # print(de1, de2)
            round1(de1, de2)


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

whole_game(deck1, deck2)

print(deck1, deck2)
score1, score2 = 0, 0
for i in range(1, len(deck1) + 1):
    score1 += deck1[-i] * i
for i in range(1, len(deck2) + 1):
    score2 += deck2[-i] * i
print(score1, score2)
