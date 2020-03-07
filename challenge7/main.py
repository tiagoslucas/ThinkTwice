from collections import Counter
import math

import sys
with open(sys.argv[1], "r") as f:
    lines = [line.rstrip() for line in f]
    numbers = [(int)(i) for i in lines[0].split(" ")]

counter = Counter(numbers)
count = 0
med = -1

for c in sorted(counter):
    if len(numbers) % 2 != 0:
        if count + counter[c] >= len(numbers) / 2:
            med = c
            break
        else:
            count += counter[c]
    else:
        if count + counter[c] > len(numbers) / 2:
            if med == -1:
                med = c
            else:
                med += c
                med /= 2
            break
        elif count + counter[c] == math.floor(len(numbers) / 2):
            med = c
            count += counter[c]
        else:
            count += counter[c]

f = open("result.txt", "w")
f.write(str(med))
f.close()
