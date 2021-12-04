def byr_ok(pasp):
    if pasp['byr'].isdigit() and 1920 <= int(pasp['byr']) <= 2002:
        return True
    return False


def iyr_ok(pasp):
    if pasp['iyr'].isdigit() and 2010 <= int(pasp['iyr']) <= 2020:
        return True
    return False


def eyr_ok(pasp):
    if pasp['eyr'].isdigit() and 2020 <= int(pasp['eyr']) <= 2030:
        return True
    return False


def hgt_ok(pasp):
    h = pasp['hgt']
    if h[:-2].isdigit():
        if h[-2:] == 'in' and 59 <= int(h[:-2]) <= 76 or h[-2:] == 'cm' and 150 <= int(h[:-2]) <= 193:
            return True
    return False


def hcl_ok(pasp):
    h = pasp['hcl']
    if h[0] == '#' and len(h) == 7:
        for sym in h[1:]:
            if not (sym.isdigit() or sym in ('a', 'b', 'c', 'd', 'e', 'f')):
                return False
        return True
    return False


def ecl_ok(pasp):
    e = pasp['ecl']
    if e in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True
    return False


def pid_ok(pasp):
    p = pasp['pid']
    if len(p) == 9:
        for sym in p:
            if not sym.isdigit():
                return False
        return True
    return False


i = 0
lst = [{}]
with open('input4.txt') as f:
    for line in f:
        if line == '\n':
            i += 1
            lst.append({})
        else:
            for field in line.rstrip().split(' '):
                lst[i][field[:3]] = field[4:]

counter = 0
for elem in lst:
    if len(elem) == 8 or len(elem) == 7 and elem.get('cid') is None:
        if (byr_ok(elem) and iyr_ok(elem) and eyr_ok(elem) and hgt_ok(elem) and hcl_ok(elem) and ecl_ok(elem) and
                pid_ok(elem)):
            counter += 1

print(counter)
