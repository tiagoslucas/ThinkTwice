from itertools import permutations
import sys

def isIncrease(perm):
	for i in range(1,len(perm)):
		if perm[i] < perm[i-1]:
			return False
	return True

def matchArr(vals, arr, l):
	for v in vals:
		isValid = False
		for i in range(0, len(arr)):
			for j in range(i+1, len(arr)):
				if arr[j] - arr[i] == v:
					isValid = True
					break
			if isValid:
				break
		if not isValid:
			return False
	return True

n = 0
vals = []
with open(sys.argv[1], 'r') as input:
	n = int(input.readline().strip())
	for i in input.readline().strip().split(' '):
		vals.append(int(i))

l = int(n * n * (n - 1) / 2)
max = sum(vals[1:])
for perm in  permutations(range(1, max), n-1):
	if isIncrease(perm):
		arr = []
		arr.append(0)
		for i in perm:
			arr.append(i)
		if matchArr(vals, arr, l):
			print(arr)
