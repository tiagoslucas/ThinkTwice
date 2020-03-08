import sys

def main():
	with open(sys.argv[1]) as input:
		for i in input:
			d = int(i.strip())
			if (d <= 5000 and d > 0):
				for i in range(10 ** 15 + 1):
					count = 0
					for j in range(1, i + 1):
						if (i % j) == 0:
							count += 1
						if count == d:
							file = open('team15_ttwins/challenge27/result.txt', 'w')
							file.write(str(i))
							file.close()
							return 0
			file = open('team15_ttwins/challenge27/result.txt', 'w')
			file.write('Impossible’')
			file.close()

if __name__ == '__main__':
	main()
