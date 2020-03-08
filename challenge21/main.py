import sys
import math
import re
def output(palavras):
    a=sorted(palavras.keys())
    fName = 'team15_ttwins/challenge21/result.txt'
    with open(fName, "w") as f:
        for i in a:

            b = sorted(palavras[i].keys())
            f.write(i+"={")
            p=1
            for j in b:
                f.write(j+"="+str(palavras[i][j]))
                if len(palavras[i]) > 1 or p<=len(palavras[i])-1:
                    if len(palavras[i]) == p:
                        f.write("}"+'\n')
                    else:
                        f.write(", ")
                elif len(palavras[i]) == p:
                    f.write("}"+'\n')
                p+=1

def readFile(path):
    with open(path,"r") as fp:
        lines = fp.readlines()
        return lines

def numFog(linhas):
    texto=[]
    for line in linhas:
        linha,nada=line.split('\n')
        if linha=='' and nada=='':
            continue    
        linha=(re.sub(r"[\W_]+", ' ',linha))
        texto.append(linha)
    texto=' '.join(texto)
    texto=texto.split(' ')
    texto=[i for i in texto if i != '']
    return texto

def dicionario(texto):
    palavras={}
    count={}
    for i in range(len(texto)-1):
        palavra1=texto[i].lower()
        palavra2=texto[i+1].lower()
        if len(palavra1)<3:
            continue
        if len(palavra1)>=3 and len(palavra2)<3:
            p=len(palavra2)
            c = 2
            while p <3:
                palavra2=texto[i+c].lower()
                p = len(palavra2)
                c +=1
        if not palavra1 in palavras:
            palavras[palavra1] = {}
        if not palavra2 in palavras[palavra1]:
            palavras[palavra1][palavra2] = 1
        else:
            palavras[palavra1][palavra2] += 1
    return palavras

def main(path):
    linhas = readFile(path)
    texto = numFog(linhas)
    a=dicionario(texto)
    output(a)

main(sys.argv[1])
