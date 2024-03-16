t = int(input())
ans = []
def calc(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

for _ in range(t):
    m, n, x, y = map(int, input().split())
    ans.append(calc(m, n, x, y))
for i in ans:
    print(i)