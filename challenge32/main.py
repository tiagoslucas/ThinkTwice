from itertools import combinations, permutations
import sys
list1 = []


def replacements(key):
    for comb in combinations(range(10), len(key)):
        for perm in permutations(comb):
            if perm[0] * perm[1] != 0:
                temp = dict(zip(key, perm))
                no0 = True
                for h in list1:
                    if temp[h] == 0:
                        no0 = False
                        continue
                if no0:
                    yield temp


with open(sys.argv[1], 'r', encoding='utf8') as f:
    numberOfWords = int(f.readline())
    list2 = []
    for i in range(numberOfWords):
        list2.append(f.readline().strip())
        if not list2[i][0] in list1:
            list1.append(list2[i][0])
    list3 = []
    for i in list2:
        for j in i:
            list3.append(j)
    list3 = set(list3)
    key = "".join(list3)

count = 0
for replacement in replacements(key):
    def f(x): return sum(replacement[e] * 10**i for i, e in enumerate(x[::-1]))
    total = 0
    for i in range(numberOfWords - 1):
        total += f(list2[i])
    if total == f(list2[-1]):
        #        print('{} + {} = {}'.format(f(list2[0]), f(list2[1]), f(list2[2])))
        count += 1

f = open('team15_ttwins/challenge32/result.txt', 'w')
f.write(str(count))
f.close()