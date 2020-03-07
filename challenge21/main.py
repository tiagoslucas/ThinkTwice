import sys
import re
import json

dic = {}
word_ant = ""
with open(sys.argv[1], 'r', encoding='utf8') as fp: 
    line = fp.readline()
    while line:
        process_line = re.split(' |-',line[:-1])
        for word in process_line:
            word = re.sub(r'[^\w\s]', '', word)
            word_act = word.lower()
            if word_ant == "":
                word_ant = word_act
            elif len(word_act) >= 3:
                if word_ant not in dic.keys():
                    dic[word_ant] = {word_act:1}
                elif word_act not in dic[word_ant].keys():
                    dic[word_ant][word_act] = 1
                else:
                    dic[word_ant][word_act] += 1
                word_ant = word_act
        line = fp.readline()

f = open('result.txt', 'w', encoding='utf8')
new_dic = {}
for key in sorted(dic.keys()) :
    new_dic[key] = dic[key]
dic = new_dic
for d in dic:
    f.write(d + '={')
    strW = ''
    for w in dic[d]:
        strW = strW + w + '=' + str(dic[d][w]) + ', '
    f.write(strW[:-2]+'}\n')
