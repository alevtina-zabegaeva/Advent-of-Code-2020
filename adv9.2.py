def search_error(lis, err):
    for j in range(len(lis)):
        summ = lis[j]
        k = 1
        while j + k < len(lis):
            summ += lis[j + k]
            if summ > err:
                break
            elif summ == err:
                return min(lis[j:j + k]) + max(lis[j:j + k])
            k += 1
    return None


with open('input9.txt') as f:
    lst = tuple(map(int, f.read().split()))

# length = 5
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
        error_num = lst[i]
        print(error_num)
        break

print(search_error(lst, error_num))
