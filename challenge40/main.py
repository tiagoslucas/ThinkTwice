import sys

with open(sys.argv[1], 'r', encoding='utf8') as f:
    num_ant = 0
    ant = []
    first = None
    for i in f:
        num_act = int(i.split("|")[0])
        act = i.split("|")[1].split(",")

        if first == None:
            first = i

        if len(act) - len(ant) != num_act:
            if len(ant) + len(act) < len(ant) + num_act:
                act = ant[: len(ant) + num_act - len(act)] + \
                    ant[-(num_act - len(act)):] + act
            else:
                act = ant[: len(ant) + num_act - len(act)] + act

        num_ant = num_act
        ant = act

    i = first
    string = ""

    f = open("result.txt", "w", encoding="utf8")
    f.write(" ".join(act).replace("\n", ""))
    f.close()
