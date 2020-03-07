from itertools import combinations
import sys

with open(sys.argv[1], "r") as f:
    count = 0
    arr = []
    for i in f:
        if count == 0:
            n = (int)(i.split(" ")[0])
            k = (int)(i.split(" ")[1])
            count += 1
        else:
            arr.append([(int)(i.split(" ")[0]), (int)(i.split(" ")[1])])


def sortArr(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] > arr[j][0]:
                temp = arr[i][0]
                arr[i][0] = arr[j][0]
                arr[j][0] = temp
    return arr


def numberOfVK(arr, k):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i][1] == arr[i - 1][1] or arr[i][1] == arr[i + 1][1]:
            return False
        if arr[i][1] > arr[i - 1][1] and arr[i][1] > arr[i + 1][1]:
            count += 1
        if arr[i][1] < arr[i - 1][1] and arr[i][1] < arr[i + 1][1]:
            count += 1
    if count == k:
        return True
    return False


total = 0
c = 1
for i in range(3, len(arr)):
    inserted = []
    for perm in list(combinations(range(0, len(arr)), i)):
        temp = []
        for index in list(perm):
            temp.append(arr[index])
        temp_sort = sortArr(temp)
        # print(c, temp_sort)
        c += 1
        if numberOfVK(temp_sort, k):
            temp_1 = []
            for l in temp_sort:
                temp_1.append(l[1])
            if not temp_1 in inserted:
                total += 1
                inserted.append(temp_1)

    # print(inserted, total)

if numberOfVK(sortArr(arr), k):
    total += 1

f = open("team15_ttwins/challenge34/result.txt", "w")
f.write(str(total))
f.close()
