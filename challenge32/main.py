import sys
import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation,arr):
    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            a = [str(get_value(word, sol)) for word in left]
            a.append(get_value(right, sol))
            arr.append(a)
    return arr     
def output(counter):
    fName = "team15_ttwins/challenge32/result.txt"
    with open(fName, "w") as f:
        f.write(str(counter)) 
def readFile(path):
    with open(path) as fp:
        lines = fp.readlines()
        return lines
            

def main(path):
    lines = readFile(path)
    palavras=[]
    for line in lines:
        linha=line.split('\n')
        palavras.append(linha[0])
    total=palavras[0]
    eq = ""
    for i in range(1,len(palavras)):
        if i < int(total)-1:
            eq += palavras[i] + " + "
        elif i == int(total)-1:
            eq += palavras[i] + " = "
        else:
            eq += palavras[i]
    arr = []
    
    a = solve2(eq,arr)
    f = 0
    counter = 0
    palavras = palavras[1:]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if not len(str(a[i][j])) == len(palavras[j]):
                f = 1
        if f == 0:
            counter += 1
        f = 0
    output(counter)
main(sys.argv[1])
