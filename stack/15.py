def push(stack, elem):
    stack.append(elem)
    return elem
def top(stack):
    return stack[-1]
def pop(stack):
    return stack.pop()
def size(stack):
    return len(stack)
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return power(a, n - 1) * a
inf = 2 * power(10, 9) + 1
n = int(input())
a = [-inf] + list(map(int, input().split())) + [-inf]
stack = []
push(stack, 0)
ans = [0] * (n + 2)
for i in range(1, n + 2):
    curr = a[i]
    while a[top(stack)] > curr:
        if i == n + 1:
            ans[pop(stack)] = -1
        else:
            ans[pop(stack)] = i - 1
    push(stack, i)
print(' '.join(list(map(str, ans[1: -1]))))
