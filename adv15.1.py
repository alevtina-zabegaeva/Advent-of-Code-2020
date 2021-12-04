# inpt = (0, 3, 6)
# inpt = (1, 3, 2)
# inpt = (2, 1, 3)
# inpt = (1, 2, 3)
# inpt = (2, 3, 1)
# inpt = (3, 2, 1)
# inpt = (3, 1, 2)
inpt = (9, 6, 0, 10, 18, 2, 1)

numbers = list(inpt)
for i in range(len(inpt) - 1, 2019):
    new_number = 0
    for j in range(len(numbers) - 2, -1, -1):
        if numbers[j] == numbers[i]:
            new_number = i - j
            break
    numbers.append(new_number)

print(numbers[-1])

'''
numbers = {i: j for j, i in enumerate(inpt)}

last_number = inpt[-1]
last_index = inpt(len) - 1
new_number = 0
next_number = 
for k in range(len(inpt) - 1, 2020):
    if new_number in numbers:
        numbers[last]
    else:
        numbers[new_number] = k
print(numbers)
'''
