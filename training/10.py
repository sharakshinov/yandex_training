N, M, K = map(int, input().split())
np = [[] for x in range(N)]
for j in range(N):
    np[j] = list(map(int, input().split()))


sq_matrix = [[0] for _ in range(N+1)]


sq_matrix[0] = [0]*(M+1)
for x in range(N):
    for y in range(M):
        sq_matrix[x+1].append(np[x][y] + sq_matrix[x+1][-1])


for i in range(M):
    for j in range(N):
        sq_matrix[j+1][i+1] += sq_matrix[j][i+1]


# combine input and solution
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    res = sq_matrix[x2][y2] - sq_matrix[x2][y1-1] - sq_matrix[x1-1][y2] + sq_matrix[x1-1][y1-1]
    print(res)
