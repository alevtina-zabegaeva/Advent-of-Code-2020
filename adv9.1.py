with open('input9.txt') as f:
    lst = tuple(map(int, f.read().split()))

length = 25
preamble = set(lst[:length])

for i in range(length, len(lst)):
    found = False
    preamble = set(lst[i - length:i])
    for p in preamble:
        if 2*p != lst[i] and lst[i] - p in preamble:
            found = True
            break
    if not found:
        print(lst[i])
        break
