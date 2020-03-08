import sys

with open(sys.argv[1], 'r') as input:
    n = int(input.read())
for i in range(10 ** 15):
	list=[]
	for num in range(1,i+1):
		if i%num == 0:
			list.append(num)
	if len(list) == n:
		file = open('team15_ttwins/challenge27/result.txt','w')
		file.write(str(num))
		file.close()
		break