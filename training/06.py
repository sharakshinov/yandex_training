M = int(input())
N = int(input())
limits = []


for i in range(N):
    limit = tuple(map(int, input().split()))
    limits.append([limit])

res = 0

for i in range(len(limits)-1, -1, -1):
    is_sec = True
    for j in range(i+1, len(limits), 1):
        if not(limits[i][0][0] > limits[j][0][1] or limits[i][0][1] < limits[j][0][0]):
            is_sec = False
    if is_sec:
        res += 1


print(res)
