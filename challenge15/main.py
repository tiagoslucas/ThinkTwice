import sys
with open(sys.argv[1]) as f:
    lines = [line.rstrip() for line in f]

n = (int)(lines[0].split(' ')[0])
m = (int)(lines[0].split(' ')[1])

step = 1
count = 0
while n < m:
    n += step
    if n - m > step:
        step = step + 1
    else:
        step = 1
    if step + 1 < n:
        step += 1
    count += 1

f = open("team15_ttwins/challenge15/result.txt", "w")
f.write(count)
f.close()
