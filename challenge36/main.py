import sys

with open(sys.argv[1], 'r', encoding='utf8') as f:
    count = 0
    d = []
    for i in f:
        if count == 0:
            n = (int)(i.strip())
        else:
            for k in i.split(" "):
                d.append((int)(k))
        count += 1

    def graphExists(a):
        while True:
            a = sorted(a, reverse=True)
            if a[0] == 0 and a[len(a) - 1] == 0:
                return True

            v = a[0]
            a = a[1:]

            if v > len(a):
                return False

            for i in range(v):
                a[i] -= 1
                if a[i] < 0:
                    return False

    if (graphExists(d)):
        isValid = True
        for i in range(1, len(d)):
            if d[i] != d[i - 1]:
                isValid = False
                break
        if not isValid:
            f = open("team15_ttwins/challenge36/result.txt", "w")
            f.write('NO')
            f.close()
        else:
            f = open("team15_ttwins/challenge36/result.txt", "w")
            f.write('YES')
            f.close()

    else:
        f = open("team15_ttwins/challenge36/result.txt", "w")
        f.write('NO')
        f.close()
