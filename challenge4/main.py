import math


def isPrime(number):
    for i in range(2, (int)(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


with open('input2.txt') as f:
    lines = [line.rstrip() for line in f]
    n, c = lines[0].split(" ")
    n = (int)(n)
    c = (int)(c)
    out = []
    for i in range(1, n + 1):
        if isPrime(i):
            out.append(i)

    result = []

    if len(out) > 2 * c:
        if len(out) % 2 == 0:
            for i in range(0, c):
                result.append(out[math.floor(len(out) / 2 - 1) + (i + 1)])
                result.append(out[math.floor(len(out) / 2) - (i + 1)])
        else:
            result.append(out[2 * c])
            for i in range(0, c-1):
                result.append(out[math.floor(len(out) / 2) - (i + 1)])
                result.append(out[math.floor(len(out) / 2) + (i + 1)])
    else:
        result = out
    f = open("result.txt", "w")
    f.write(str(n) + " " + str(c) + ": " +
            str(sorted(result))[1:-1].replace(",", ""))
    f.close()
