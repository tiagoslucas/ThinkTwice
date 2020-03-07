from heapq import heappush, heappop
import sys
import string
cb = [[0 for x in range(8)] for y in range(8)]
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def main(filename):
    board = [["{0:0=2d}".format(x+y*8) for x in range(8)] for y in range(8)]
    visit = [[0 for x in range(8)] for y in range(8)]
    initial = -1

    with open(filename,'r') as file:
        for i in file:
            initial = i

    with open('result.txt', 'w') as file:
        for k in range(64):
            cb[ky][kx] = k + 1
            pq = []
            for i in range(8):
                nx = kx + dx[i]; ny = ky + dy[i]
                if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
                    if cb[ny][nx] == 0:
                        ctr = 0
                        for j in range(8):
                            ex = nx + dx[j]; ey = ny + dy[j]
                            if ex >= 0 and ex < 8 and ey >= 0 and ey < 8:
                                if cb[ey][ex] == 0: ctr += 1
                        heappush(pq, (ctr, i))
            if len(pq) > 0:
                (p, m) = heappop(pq)
                kx += dx[m]; ky += dy[m]
            else:
                break

        for cy in range(8):
            for cx in range(8):
                file.write(str(cb[cy][cx]) + '\n', 2)
            file.write('\n')

if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1])
