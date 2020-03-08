import sys
def output(a):
    fName = 'team15_ttwins/challenge35/result.txt'
    with open(fName, "w") as f:
        if len(a) > 7:
            f.write('ERROR')
        else:
            f.write(str(a))
def readFile(path):
    with open(path) as fp:
        n,b1,b2 = fp.readline().strip("\n").split(" ")
        return n,int(b1),int(b2)
SY2VA = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'A': 10,
         'B': 11,
         'C': 12,
         'D': 13,
         'E': 14,
         'F': 15
}
def str2int(string, base):
    integer = 0
    for character in string:
        value = SY2VA[character]
        integer *= base
        integer += value
    return integer

VA2SY = dict(map(reversed, SY2VA.items()))

def int2str(integer, base):
    array = []
    while integer:
        integer, value = divmod(integer, base)
        array.append(VA2SY[value])
    return ''.join(reversed(array))

def go(innitvar,basevar,convertvar):
    integer = 0
    for character in innitvar:
        value = SY2VA[character]
        integer *= basevar
        integer += value
    VA2SY = dict(map(reversed, SY2VA.items()))
    array = []
    while integer:
        integer, value = divmod(integer, convertvar)
        array.append(VA2SY[value])
    answer = ''.join(reversed(array))
    return answer
def main(path):
    n,b1,b2 = readFile(path)
    a = go(n,b1,b2)
    output(a)
main(sys.argv[1])