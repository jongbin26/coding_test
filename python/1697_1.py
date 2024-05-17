from collections import deque
n, k = map(int, input().split())
visited = [0] * (100000 * 2)
def bfs():
    queue = deque()
    queue.append((n, 0))
    visited[n] = 1
    while queue:
        x, cnt = queue.popleft()
        if x == k:
            return cnt
        if x - 1 >= 0 and not visited[x-1]:
            visited[x-1] = 1
            queue.append((x-1, cnt+1))
        if x + 1 < 100000 * 2 and not visited[x+1]:
            visited[x+1] = 1
            queue.append((x+1, cnt+1))
        if 2 * x < 100000*2 and not visited[2*x]:
            visited[2*x] = 1
            queue.append((2*x, cnt+1))
print(bfs())