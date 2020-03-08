import sys

def knightTour(N, initX, initY):
    def isSafe(x, y):
        if 0 <= x < N and 0 <= y < N and board[x][y] == -1:
            return True
        return False

    def backtrack(cur_x, cur_y, moveCount):
        if moveCount >= N*N:
            return True

        for i in range(8):
            next_x = cur_x + move_x[i]
            next_y = cur_y + move_y[i]

            if isSafe(next_x, next_y):
                board[next_x][next_y] = moveCount

                if backtrack(next_x, next_y, moveCount+1):
                    return True

                board[next_x][next_y] = -1

        return False

    board = [[-1 for i in range(N)] for j in range(N)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[initX][initY] = 0
    backtrack(0, 0, 1)
    return board

file = open(sys.argv[1], 'r')
var = file.read().split()
N = int(var[0])
x = int(var[2])//int(var[1])
y = int(var[2])%int(var[1])
file.close()

result = knightTour(N, x, y)
file = open('team15_ttwins/challenge18/result.txt', 'w')
for line in result:
    l = ""
    for n in line:
        l += "%02d " % (n,)
    file.write(l[:-1] + '\n')
file.close()