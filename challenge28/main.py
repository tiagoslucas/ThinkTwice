import sys

def collatz(n):
    seq = []
    while n > 1:
        seq.append(n)
        # print(n, end=' ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    return seq
 
seqOfSeqs = {}
seqOfSeqs2 = {}

with open(sys.argv[1], 'r') as input:
    n = input.read()

for i in range(int(n)):
    seqFinal = collatz(i)
    seqOfSeqs[i] = len(seqFinal)
    seqOfSeqs2[i] = seqFinal
max1 = max(seqOfSeqs, key=seqOfSeqs.get)

f = open('team15_ttwins/challenge28/result.txt', 'w')
f.write(str(max1) + " " + str(len(seqOfSeqs2[max1])))
f.close()
