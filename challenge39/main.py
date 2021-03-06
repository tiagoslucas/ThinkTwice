from itertools import combinations_with_replacement, permutations
from functools import reduce
from math import gcd
import sys
import re

dict1 = {}
dict2 = {}
list1 = []
list2 = []
result = []


def dictFromList(listName):
    dictName = {}
    for i in listName:
        v = re.sub('([A-Z][a-z])', r' \1',
                   re.sub('([A-Z])', r' \1', i)).split()
        for j in v:
            if re.search('[0-9]', j) is not None:
                n = re.search('[0-9]', j)[0]
                m = re.sub('[0-9]', '', j)
                if m in list(dictName.keys()):
                    dictName.update({m: int(n) + int(dictName[m])})
                else:
                    dictName.update({m: n})
            else:
                if j in list(dictName.keys()):
                    dictName.update({j: 1 + (int)(dictName[j])})
                else:
                    dictName.update({j: 1})
    return dictName


def create_combinations(firstList, secondList):
    elements = list(dictFromList(firstList).keys())
    for i in elements:
        if i not in dictFromList(secondList).keys():
            print(i, dictFromList(secondList).keys())
            return 1

    for comb in combinations_with_replacement(range(1, 10), (len(firstList) + len(secondList))):
        for perm in permutations(comb):
            fList = []
            sList = []
            for i in range(len(perm)):
                if i < len(firstList):
                    for x in range(int(perm[i])):
                        fList.extend([firstList[i]])
                else:
                    for x in range(int(perm[i])):
                        sList.extend([secondList[i - len(firstList)]])

            for j in dictFromList(fList).keys():
                if dictFromList(fList)[j] != dictFromList(sList)[j]:
                    break
            else:
                for i in perm:
                    result.append(i)
                firstList = fList
                secondList = sList
                return 0
    return 1


with open(sys.argv[1], 'r') as input:
    eq = input.readline()
    arg1, arg2 = eq.split('=')
    list1 = arg1.split('+')
    list2 = arg2.split('+')

if create_combinations(list1, list2) == 1:
    with open('team15_ttwins/challenge39/result.txt', 'w') as output:
        output.write('IMPOSSIBLE')
else:
    div = reduce(gcd, result)
    with open('team15_ttwins/challenge39/result.txt', 'w') as output:
        output.writelines(f"{int(i/div)} " for i in result)
