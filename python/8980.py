import heapq
N, C = map(int, input().split())
M = int(input())
info = [list(map(int, input().split())) for _ in range(M)]

info.sort(key = lambda a : a[0])
info.sort(key = lambda a : a[1])
ans = 0
station = [0] * (N+1)
for i in info:
    tmp = True
    if max(station[i[0]:i[1]]) + i[2] <= C:
        for j in range(i[0], i[1]):
            station[j] += i[2]
        ans += i[2]
    else:
        last = C - max(station[i[0]:i[1]])
        for j in range(i[0], i[1]):
            station[j] += last
        ans += last
print(ans)