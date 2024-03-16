n, m, b = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

ans_time, height = int(1e9), 0

for h in range(0, 257):
    total, minus, plus = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if data[i][j] - h > 0:
                minus += data[i][j] - h
            else:
                plus += h - data[i][j]
    total = 2 * minus + plus
    if total <= ans_time and minus + b >= plus:
        ans_time, height = total, h

print(ans_time, height)
