with open('input2.txt') as f:
    lines = [line.rstrip() for line in f]
    number = lines[0]

numbers = [(int)(n) for n in number.split("^")]


def decompose(n):
    pows = []
    while (n != 1):
        for k in range(2, int(n) + 1):
            if n % k == 0:
                pows.append(int(k))
                n /= k
                break
    return pows


all = []
for n in numbers:
    temp = []
    for k in decompose(n):
        temp.append(k)
    all.append(temp)

print(all)
