import sys

def output(sol):
    fName = "team15_ttwins/challenge1/result.txt"
    with open(fName, "w") as f:
        f.write(str(sol))

def readFile(path):
    n=int()
    p=int()
    a=[]
    with open(path) as fp:
        for line in fp:
            line = line.strip("\n")
            a.append(line)
    n=int(a[0])
    p=int(a[1])
    return n,p
           

def main(path):
    n,p=readFile(path)
    sol = 0
    while p != sol**n:
        sol+=1
    output(sol)

main(sys.argv[1])