# card_key = 5764801  # test
# door_key = 17807724  # test
card_key = 8252394
door_key = 6269621
val = 20201227
subject_number = 7

number = 1
for i in range(10000000):
    number *= subject_number
    number = number % val
    # print(i + 1, number)
    if number == card_key:
        card_loop = i + 1
        print("card's loop number =", i + 1, "card's key =", number)
    elif number == door_key:
        door_loop = i + 1
        print("door's loop number =", i + 1, "door's key =", number)

number = 1
for i in range(door_loop):
    number *= card_key
    number = number % val
print(number)
'''
number = 1
for i in range(card_loop):
    number *= door_key
    number = number % val
print(number)
'''
