def search_sum():
    for element1 in lst:
        for element2 in lst:
            for element3 in lst:
                if element1 + element2 + element3 == 2020:
                    return(element1 * element2 * element3)

lst = []
with open('input1.txt') as f:
    for line in f:
        lst.append(int(line))

print(search_sum())