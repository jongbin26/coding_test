from collections import deque
n, a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def bfs(x):
    queue = deque()
    queue.append((x,0))
    while queue:
        x, total = queue.popleft()
        if x == b:
            return total
        for next, len in graph[x]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, total+len))
                
print(bfs(a))