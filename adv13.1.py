with open('input13.txt') as f:
    number = int(f.readline())
    lst = tuple(int(i) for i in f.readline().split(',') if i.isdigit())

rest = []
minimum = 1000
for i, n in enumerate(lst):
    rest.append(n - number % n)
    if minimum > rest[-1]:
        minimum = rest[-1]
        minimum_ind = i

print(minimum * lst[minimum_ind])
