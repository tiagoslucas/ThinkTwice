from itertools import product
import sys 
validTuple = []
n = 0
with open(sys.argv[1], 'r', encoding="utf8") as f:
    n = int(f.read())

for i in [p for p in product([0,1],repeat=n)]:
    prev = i[0]
    isValidTuple = True
    for j in range(1,len(i)):
        if i[j] == prev and prev == 1:
            isValidTuple = False
            break
        if j == len(i)-1 and i[j] == i[0] and i[j] == 1:
            isValidTuple = False
            break
        prev = i[j]
    
    if isValidTuple:
        validTuple.append(i)

f = open("team15_ttwins/challenge29/result.txt", "w")
f.write(len(validTuple))
f.close()