N = int(input())
c = []
res = 0
for i in range(N):
    i = int(input())
    c.append(i)
for i in range(len(c)-1):
    m = min(c[i], c[i+1])
    res += m
print(res)
