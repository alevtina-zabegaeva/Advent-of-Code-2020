def read_file():
    lst = []
    with open('input1.txt') as f:
        for line in f:
            lst.append(int(line))
            for element in lst:
                if element + lst[-1] == 2020:
                    print(element * lst[-1])
                    return


read_file()
