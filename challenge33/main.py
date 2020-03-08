import sys
import math

with open(sys.argv[1], 'r', encoding="utf8") as f:
    count = 0
    cords = []
    for i in f:
        if (int)(count) == 0:
            k = (int)(i.split(" ")[1])
            n = (int)(i.split(" ")[0])
        else:
            temp = i.split(" ")
            cords = list(zip(temp[::2], temp[1::2]))
        count += 1
    centroids = {
        i+1: [cords[i][0], cords[i][1]]
        for i in range(k)
    }

    def distanceBetween(a, b):
        return math.sqrt(((int)(a[0]) - (int)(b[0])) ** 2 + ((int)(a[1]) - (int)(b[1])) ** 2)
    iteractions = 0
    while iteractions < 1000:
        clusters = {}
        for i in range(k):
            clusters[i] = []

        for cord in cords:
            dist = -1
            mean = -1
            for centroid in centroids:
                c = centroids[centroid]
                new_dist = distanceBetween(cord, c)
                if dist == -1:
                    dist = new_dist
                    mean = centroid
                else:
                    if new_dist < dist:
                        dist = new_dist
                        mean = centroid
            clusters[mean-1].append(cord)

        for centroid in centroids:
            x = 0
            y = 0
            for point in clusters[centroid-1]:
                x += (int)(point[0])
                y += (int)(point[1])
            x = x / len(clusters[centroid - 1])
            y = y / len(clusters[centroid - 1])
            centroids[centroid] = [x, y]

        iteractions += 1

    dists = 0
    arr = []
    for cluster in clusters:
        x = 0
        y = 0
        for point in clusters[cluster]:
            x += (int)(point[0])
            y += (int)(point[1])
        x /= len(clusters[cluster])
        y /= len(clusters[cluster])
        arr.append(distanceBetween(clusters[cluster][0], [x, y]))

    f = open("team15_ttwins/challenge33/result.txt", "w")
    f.write(f"{max(arr):.2f}")
    f.close()
