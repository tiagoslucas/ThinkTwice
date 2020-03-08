import sys

with open(sys.argv[1], 'r') as input:
	n = int(input.readline().strip())
	leituras = n * n * (n - 1) / 2
	