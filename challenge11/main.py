# with open('input2.txt') as f:
#     lines = [line.rstrip() for line in f]
#     number = lines[0]

# numbers = [(int)(n) for n in number.split("^")]


# def decompose(n):
#     pows = []
#     while (n != 1):
#         for k in range(2, int(n) + 1):
#             if n % k == 0:
#                 pows.append(int(k))
#                 n /= k
#                 break
#     return pows


# def powerOf(numbers):
#     print(numbers)
#     n = numbers[0]
#     prod = -1
#     for i in range(1, len(numbers)):
#         if prod == -1:
#             print(numbers[-i - 1], numbers[-i])
#             prod = numbers[-i - 1] ** numbers[-i]
#         else:
#             print(numbers[-i - 1], prod)
#             prod = numbers[-i - 1] ** prod
#     print(prod)


# all = []
# for n in numbers:
#     for k in decompose(n):
#         all.append(k)

# powerOf(all)
