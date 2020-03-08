import sys

def main():
	with open(sys.argv[1]) as input:
		for i in input:
			d = int(i.strip())
			for i in range(10 ** 15 + 1):
				count = 0
				for j in range(1, i):
					if (i % j) == 0:
						count += 1
					if count == d:
						file = open('team15_ttwins/challenge35/result.txt', 'w')
						file.write(str(d))
						file.close()
						return 0

if __name__ == '__main__':
	main()