with open('input1.txt') as f:
    lines = [line.rstrip() for line in f]
    colors = lines[0].split(" ")

matrix = []
for i in range(1, len(lines)):
    matrix.append(lines[i].split(" "))
