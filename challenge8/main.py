import sys

def main(filename):
	board = [["{0:0=2d}".format(x+y*8) for x in range(8)] for y in range(8)]
	visit = [[0 for x in range(8)] for y in range(8)]
	initial = -1

	with open(filename,'r') as file:
		for i in file:
			initial = i

	with open('result.txt', 'w') as file:
		file.write(final)

if __name__ == '__main__' and len(sys.argv) > 1:
	main(sys.argv[1])
