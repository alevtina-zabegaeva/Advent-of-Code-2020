def number_add(dict_numbers, number2add, index):
    if number2add in dict_numbers:
        numbers[number2add] = numbers[number2add] + [index]
        if len(dict_numbers[number2add]) > 2:
            dict_numbers[number2add] = dict_numbers[number2add][1:]
    else:
        dict_numbers[number2add] = [index]
    return dict_numbers

# inpt = (0, 3, 6)
# inpt = (1, 3, 2)
# inpt = (2, 1, 3)
# inpt = (1, 2, 3)
# inpt = (2, 3, 1)
# inpt = (3, 2, 1)
# inpt = (3, 1, 2)
inpt = (9, 6, 0, 10, 18, 2, 1)

numbers = {k: [j] for j, k in enumerate(inpt)}

# print(numbers)
last_number = inpt[-1]
for i in range(len(inpt), 30000000):
    new_number = numbers[last_number][-1] - numbers[last_number][0]
    numbers = number_add(numbers, new_number, i)
    last_number = new_number

# print(numbers)
print(last_number)
