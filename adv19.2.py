def calc(rule_number):
    if type(rules[rule_number]) == str:
        return [rules[rule_number]]
    else:
        result_list = []
        if len(rules[rule_number]) == 1:
            if len(rules[rule_number][0]) == 1:
                result_list = calc(rules[rule_number][0][0]).copy()
            else:
                result_list1 = []
                for x in calc(rules[rule_number][0][0]):
                    for y in calc(rules[rule_number][0][1]):
                        result_list.append(x + y)
                if len(rules[rule_number][0]) > 2:
                    for x in result_list:
                        for y in calc(rules[rule_number][0][2]):
                            result_list1.append(x + y)
                    result_list = result_list1.copy()
            return result_list
        else:
            if len(rules[rule_number][0]) == 1:
                result_list = calc(rules[rule_number][0][0]).copy()
            else:  # FIXME kann auch 3 sein
                for x in calc(rules[rule_number][0][0]):
                    for y in calc(rules[rule_number][0][1]):
                        result_list.append(x + y)
            if len(rules[rule_number][1]) == 1:
                result_list.extend(calc(rules[rule_number][1][0]))
            else:  # FIXME kann auch 3 sein
                for x in calc(rules[rule_number][1][0]):
                    for y in calc(rules[rule_number][1][1]):
                        result_list.append(x + y)
            return result_list


entities = []
rules = {}
isrules = True
with open('input19.2.txt') as f:
    for line in f:
        if isrules:
            if line != '\n':
                i = line.find(':')
                line1 = int(line[:i])
                line2 = line[i + 2:].rstrip()
                if line2[-1] == '"':
                    line2 = line2[1]
                elif line2.count('|') > 0:
                    line2 = line2.split('|')
                    for k in range(len(line2)):
                        line2[k] = [int(j) for j in line2[k].strip().split(' ')]
                else:
                    line2 = [[int(j) for j in line2.split(' ')]]
                rules[line1] = line2
            else:
                isrules = False
        else:
            entities.append(line.rstrip())

print(rules)
print(entities)

decisions31 = calc(31)
decisions31 = set(decisions31)
decisions42 = calc(42)
decisions42 = set(decisions42)

entities2 = []
entities3 = []
for ent in entities:
    entities3.append([])
    entities2.append(True)
    is42 = True
    counter42 = 0
    counter31 = 0
    for ii in range(0, len(ent), 8):
        e = ent[ii:ii + 8]
        if e in decisions42:
            counter42 += 1
            entities3[-1].append(42)
            if not is42:
                entities2[-1] = False
        else:
            counter31 += 1
            entities3[-1].append(31)
            is42 = False
            if counter42 == 0:
                entities2[-1] = False
    if counter42 < 2 or counter31 < 1 or counter42 <= counter31:
        entities2[-1] = False

for i in range(len(entities2)):
    print(entities2[i], entities3[i])
print(sum(entities2))
