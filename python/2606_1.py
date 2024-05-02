from collections import deque
n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True
    count = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1
    return count
print(bfs())