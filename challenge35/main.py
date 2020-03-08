from itertools import combinations_with_replacement, permutations
import sys

with open(sys.argv[1], 'r') as input:
    vars = input.readline().split(' ')
    m = vars[0]
    t = vars[1]
    instructions = input.readline().split(' ')

dictInstruction = {}

index = 0
for instruction in instructions:
    if instruction == 'L':
        dictInstruction[index] = 'ans'
    elif instruction == 'o':
        dictInstruction[index] = 0
    elif instruction.find('+') != -1:
        print(instruction)
        dictInstruction[index]  = int(instruction.replace('+',''))
        print(dictInstruction[index])
    else:
        dictInstruction[index] = int(instruction)
    index += 1

list = []
if int(t) == 1:
    list = {(1), (2)}
else:
    for comb in (combinations_with_replacement(range(1,3),int(t))):
            for perm in permutations(comb):
                list.append(perm)
    list = set(list)
turn = 0
notFav = 0
for perm in list:
    house = 0
    index = 0
    if int(t) == 1:
        house = house + perm
    else:
        for i in perm:
            if (dictInstruction[perm[index]] != 'ans'):
                house = house + perm[index] + dictInstruction[perm[index]]
            if(house >= int(m)+1):
                exit
            index += 1
            if(index == int(t)):
                exit
    if house < (int(m) + 1):
        notFav += 1

prob = 1-(notFav/len(list))

f = open('result.txt', 'w')
# f = open('team15_ttwins/challenge35/result.txt', 'w')
if prob > 0.5:
    f.write(f"Bet for. {prob:.4f}")
elif prob < 0.5:
    f.write(f"Bet against. {prob:.4f}")
else:
    f.write(f"Push. {prob:.4f}")

f.close()
