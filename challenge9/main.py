with open('input2.txt') as f:
    lines = [line.rstrip() for line in f]
    length, mult = lines[0].split(" ")

length = (int)(length)
mult = (int)(mult)

if length % 2 == 0:
    numb_zeros = length / 2

numbers = []
for i in range(0, (int)(numb_zeros)):
    numbers.append(0)
    numbers.append(1)


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            if not [m] + p in l:
                l.append([m] + p)
    return l


permutations = permutation(numbers)


def isMultiple(value, mult):
    binary = ""
    for i in value:
        binary += str(i)
    if int(binary, 2) % mult == 0 and int(binary, 2) >= 2**(length-1):
        print(binary, int(binary, 2), mult, int(binary, 2) / mult)
        return True
    return False


count = 0

for permutation in permutations:
    if isMultiple(permutation, mult):
        count += 1

f = open("result.txt", "w")
f.write(str(count))
f.close()
