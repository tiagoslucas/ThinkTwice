import sys

import queue


def containsOdd(G, src):
    global V

    # Create a color array to store
    # colors assigned to all veritces.
    # Vertex number is used as index
    # in this array. The value '-1' of
    # colorArr[i] is used to indicate
    # that no color is assigned to vertex
    # 'i'. The value 1 is used to indicate
    # first color is assigned and value 0
    # indicates second color is assigned.
    colorArr = [-1] * V

    # Assign first color to source
    colorArr[src] = 1

    # Create a queue (FIFO) of vertex
    # numbers and enqueue source vertex
    # for BFS traversal
    q = queue.Queue()
    q.put(src)

    # Run while there are vertices in
    # queue (Similar to BFS)
    while (not q.empty()):

        # Dequeue a vertex from queue
        u = q.get()

        # Return true if there is a self-loop
        if (G[u][u] == 1):
            return True

        # Find all non-colored adjacent vertices
        for v in range(V):

            # An edge from u to v exists and
            # destination v is not colored
            if (G[u][v] and colorArr[v] == -1):

                # Assign alternate color to this
                # adjacent v of u
                colorArr[v] = 1 - colorArr[u]
                q.put(v)

            # An edge from u to v exists and
            # destination v is colored with
            # same color as u
            elif (G[u][v] and
                  colorArr[v] == colorArr[u]):
                return True

    # If we reach here, then all
    # adjacent vertices can be
    # colored with alternate color
    return False


with open(sys.argv[1], 'r', encoding='utf8') as f:
    count = 0
    d = []
    for i in f:
        if count == 0:
            n = (int)(i.strip())
        else:
            for k in i.split(" "):
                d.append((int)(k))
        count += 1

    def graphExists(a):
        while True:
            a = sorted(a, reverse=True)
            if a[0] == 0 and a[len(a) - 1] == 0:
                return True

            v = a[0]
            a = a[1:]

            if v > len(a):
                return False
            for i in range(v):
                a[i] -= 1
                if a[i] < 0:
                    return False

    if (graphExists(d)):
        # Python3 program to generate a graph
        # for a given fixed degrees

        # A function to print the adjacency matrix.

        # n is number of vertices
        degseq = d
        n = len(d)
        mat = [[0] * n for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                # For each pair of vertex decrement
                # the degree of both vertex.
                if (degseq[i] > 0 and degseq[j] > 0):
                    degseq[i] -= 1
                    degseq[j] -= 1
                    mat[i][j] = 1
                    mat[j][i] = 1
        V = len(d)
        isValid = True
        if containsOdd(mat, 0):
            isValid = False
        # This code is contributed by PranchalK
        if not isValid:
            f = open("team15_ttwins/challenge36/result.txt", "w")
            f.write('NO')
            f.close()
        else:
            f = open("team15_ttwins/challenge36/result.txt", "w")
            f.write('YES')
            f.close()

    else:
        f = open("team15_ttwins/challenge36/result.txt", "w")
        f.write('NO')
        f.close()
