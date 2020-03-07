import sys
with open(sys.argv[1], "r") as f:
    lines = [line.rstrip() for line in f]
    n, l, r = lines[0].split(" ")

n = (int)(n)
l = (int)(l)
r = (int)(r)

out = [i for i in range(1, n + 1)]


def visible(permutation, side):
    count = 0
    max_col = permutation[0]
    if side == "l":
        for i in range(1, len(permutation)):
            if permutation[i] > max_col:
                max_col = permutation[i]
                count += 1
    else:
        permutation = list(reversed(permutation))
        max_col = permutation[0]
        for i in range(1, len(permutation)):
            if permutation[i] > max_col:
                max_col = permutation[i]
                count += 1
    return count + 1


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


total = 0
for i in permutation(out):
    if visible(i, "l") == l and visible(i, r) == r:
        total += 1

f = open("result.txt", "w")
f.write(str(total))
f.close()
