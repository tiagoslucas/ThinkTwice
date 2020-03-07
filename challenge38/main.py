import sys


def fiblike(start):
    addnum = len(start)
    memo = start[:]

    def fibber(n):
        try:
            return memo[n]
        except IndexError:
            ans = sum(fibber(i) for i in range(n-addnum, n))
            memo.append(ans)
            return ans
    return fibber


with open(sys.argv[1]) as f:
    for i in f:
        n, k = i.split(" ")
n = (int)(n)
k = (int)(k)

if k == 1:
    seq = [1] + [2 ** i for i in range(100)]
else:
    fibber = fiblike([1] + [2**i for i in range(k-1)])
    seq = [fibber(i) for i in range(100)]


def nearestSmallerEqFib(n, seq):
    for i in range(1, len(seq)):
        if n < seq[i]:
            return seq[i-1]


def printFibRepresntation(n, seq):
    arr = []
    while n > 0:
        for i in range(0, len(seq)):
            if seq[i] > n:
                n = n - seq[i - 1]
                arr.append(seq[i - 1])
                break
    return arr[-1]


if n in seq[2:]:
    f = open("result.txt", "w")
    f.write("lose")
    f.close()
else:
    f = open("result.txt", "w")
    f.write(str(printFibRepresntation(n, seq)))
    f.close()
