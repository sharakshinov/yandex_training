N = int(input())
K = int(input())

row = int(input())
place = int(input())

# Option_Petya
option = (row - 1) * 2 + place
ans = [0, 0]


if (option + K) <= N:
    ans[0] = (option + K + 1) // 2
    ans[1] = 2 if (K + option) % 2 == 0 else 1

# Check ahead place
if (option - K) >= 1:
    if row - ((option - K + 1) // 2) < abs(ans[0] - row):
        ans[0] = (option - K + 1) // 2
        ans[1] = 2 if (option - K) % 2 == 0 else 1
if ans[0] == 0:
    print(-1)
else:
    print(ans[0], ans[1], end=' ')
