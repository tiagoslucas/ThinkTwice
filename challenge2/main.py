import sys
f = open(sys.argv[1], "r")
text = f.read()
output = ""

for i in range(0, len(text)):
    if text[i] == "\"":
        if i % 2 == 0:
            output += "``"
        else:
            output += "''"
    else:
        if text[i:].find("\"") == -1:
            output += text[i:]
            break
        else:
            output += text[i]

f = open("team15_ttwins/challenge2/result.txt", "w")
f.write(output)
f.close()
