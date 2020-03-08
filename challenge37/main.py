import sys

vals = []
result = [0]

def assignResult(n):
	for i in range(n):
		if( i > result[len(result) - 1] ):
			result.append(vals.pop() - result[-1:])
	result.append(vals[n])
	assignResult(n-1)

with open(sys.argv[1], 'r') as file:
	n = int(file.readline())
	for i in file.readline().split(' '):
		vals.append(i)
	assignResult(n)
	file = open('result.txt', 'w')
	file.writelines(res for res in result)
	file.close()
