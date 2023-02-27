n = int(input())
height = []
width = []
for i in range(n):
    x, y = map(int, input().split())
    width.append(x)
    height.append(y)

print(min(width), min(height), max(width), max(height))
