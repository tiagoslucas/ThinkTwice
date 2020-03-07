import sys
import re
import itertools
from collections import Counter

#Read file and spli text into words
file = open(sys.argv[1], 'r', encoding='utf8')
text = re.sub(r'[^\w\s\-]', '', file.read())
all_words = text.split()

#Count words occurence in text
words = Counter()
for word in all_words:
    words[word] += 1

#Sort words by occurences
words = sorted(words, key=lambda k: (words[k]), reverse=True)

def value(n):
    dict = []
    for x in generator(n):
        dict.append(''.join(x))
    return dict

def generator(n):
    dict = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    yield from itertools.product(*([dict] * n))
    
index = 0
n = 1
values = value(n)

word_values = []
for word in words:
    word_values.append(''.join(values[index]))
    index += 1
    if index == len(values):
        index = 0
        n += 1
        values = value(n)

words = dict(zip(words, word_values))
result = '{'
for word in words:
    result += word + '=' + words[word] + ', '

result = result[:-2]
result += '}'

f = open('team15_ttwins/challenge25/result.txt', 'w', encoding='utf8')
f.write(result)
f.write('\n')
with open(sys.argv[1], 'r', encoding='utf8') as fp: 
    line = fp.readline()
    while line:
        process_line = line[:-1].split(' ')
        for word in process_line:
            word = re.sub(r'[^\w\s\-]', '', word)
            if len(word) > 0:
                line = line.replace(word, str(words[word]), 1)
        f.write(line)
        line = fp.readline()

f.close()