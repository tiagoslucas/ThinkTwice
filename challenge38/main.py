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

fibber = fiblike([1] + [2**i for i in range(1)])
fib = [fibber(i) for i in range(100)]


def nearestSmallerEqFib(n, seq):
    for i in range(1, len(seq)):
        if n < seq[i]:
            return seq[i-1]


def printFibRepresntation(n, seq):
    arr = []
    while n > 0:
        for i in range(1, len(seq)):
            if seq[i] > n:
                n = n - seq[i - 1]
                arr.append(seq[i - 1])
                break
    return arr


# Esta a usar a n-sequencia
if n in seq[2:]:
    f = open("result.txt", "w")
    f.write("lose")
    f.close()
else:
    var = -1
    if k == 1:
        if n % 2 != 0:
            var = 1
    else:
        for i in range(1, n):
            if n - i in seq[2:]:
                if i * k >= n - i:
                    isValid = False
                    for l in list(reversed(range(1, i))):
                        if l * k < n - l:
                            var = l
                            isValid = True
                            break
                    if isValid:
                        break
                else:
                    var = i
                    break

    f = open("team15/challenge38/result.txt", "w")
    f.write(str(var))
    f.close()
