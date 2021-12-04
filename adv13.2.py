def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return x, y, a


with open('input13.txt', ) as f:
    f.readline()
    lst = tuple(f.readline().split(','))

c = []
m = []
for i, n in enumerate(lst):
    if n.isdigit():
        int_n = int(n)
        m.append(int_n)
        c.append((int_n - i) % int_n)
summ = 0
for i in range(len(m)):
    mk = 1
    for j, m2 in enumerate(m):
        if i != j:
            mk *= m2
    xk = bezout(mk, m[i])[0]
    summ += mk * xk * c[i]
summ = summ % (mk * m[-1])
print(summ)
