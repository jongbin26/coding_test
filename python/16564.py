n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]
start, end = 0, max(levels) + k
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for level in levels:
        if level < mid:
            cnt += mid - level
    if cnt <= k:
        start = mid + 1
    if cnt > k:
        end = mid - 1
print(end)