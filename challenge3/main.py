import sys
with open(sys.argv[1], "r") as f:
    lines = [line.rstrip() for line in f]
swaps = 0
lines[1] = [value for value in lines[1].split(" ")]
for i in range(0, len(lines[1])):
    for j in range(i + 1, len(lines[1])):
        if lines[1][i] > lines[1][j]:
            temp = lines[1][i]
            lines[1][i] = lines[1][j]
            lines[1][j] = temp
            swaps += 1

f = open("team15_ttwins/challenge3/result.txt", "w")
f.write("Optimal train swapping takes " + str(swaps) + " swaps.")
f.close()
