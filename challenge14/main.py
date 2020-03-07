import sys
with open(sys.argv[1]) as f:
    lines = [line.rstrip() for line in f]
    init_colors = lines[0].split(" ")
dic = {}
colors = {}
for i in range(1, len(lines)):
    j = lines[i].split(" ")
    dic[j[0]] = []
    dic[j[1]] = []

for i in range(1, len(lines)):
    j = lines[i].split(" ")
    dic[j[0]].append(j[1])
    dic[j[1]].append(j[0])
    colors[j[0]] = -1
    colors[j[1]] = -1

for l in colors:
    used = []
    for k in dic[l]:
        used.append(colors[k])
    for i in range(0, len(init_colors)):
        if not i in used:
            colors[l] = i
            break

isValid = True
for color in colors:
    if colors[color] == -1:
        isValid = False
        break
    else:
        for c in dic[l]:
            if colors[c] == colors[color]:
                isValid = False
                break

if isValid:
    f = open("result.txt", "w")
    for color in colors:
        f.write(color + " " + init_colors[colors[color]] + "\n")
    f.close()
else:
    f = open("result.txt", "w")
    f.close()
