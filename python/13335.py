from collections import deque
n, w, l = map(int, input().split())
arr = list(map(int, input().split()))
weight, cnt, ans = 0, 0, 0
for i in arr:
    if weight + i < l:
        weight += i
        cnt += 1
        continue
    else:
        ans += cnt + w
        weight, cnt = 0, 0
        weight += i
        cnt += 1
ans += cnt
print(ans)