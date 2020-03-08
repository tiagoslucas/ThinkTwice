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

def sortArr(arr1):
    for iii in range(0, len(arr1)):
        for jjj in range(iii + 1, len(arr1)):
            if arr1[iii][0] > arr1[jjj][0]:
                temp_111 = arr1[iii]
                arr1[iii] = arr1[jjj]
                arr1[jjj] = temp_111
    return arr1

def numberOfVK(arr2, k):
    count = 0
    for i in range(1, len(arr2) - 1):
        if arr2[i][1] == arr2[i - 1][1] or arr2[i][1] == arr2[i + 1][1]:
            return False
        if arr2[i][1] > arr2[i - 1][1] and arr2[i][1] > arr2[i + 1][1]:
            count += 1
        if arr2[i][1] < arr2[i - 1][1] and arr2[i][1] < arr2[i + 1][1]:
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
        c += 1
        if numberOfVK(temp_sort, k):
            temp_1 = []
            for l in temp_sort:
                temp_1.append(l[1])
            if not temp_1 in inserted:
                total += 1
                inserted.append(temp_1)

if numberOfVK(sortArr(arr), k):
    total += 1

f = open("team15_ttwins/challenge34/result.txt", "w")
f.write(str(total))
f.close()
