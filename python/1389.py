from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
def bfs(x, y, cnt):
    visited[x] = 1
    queue = deque()
    queue.append((x, y, cnt))
    while queue:
        x, y, cnt = queue.popleft()
        if x == y:
            return cnt
        for i in edge[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append((i, y, cnt+1))
ans = [int(1e9), 0]
for i in range(1, n+1):
    kevin_bacon = 0
    for j in range(1, n+1):
        if i != j:
            visited = [0] * (n+1)
            kevin_bacon += bfs(i, j, 0)
    if kevin_bacon < ans[0]:
        ans = [kevin_bacon, i]
print(ans[1])