from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    x = queue.popleft()
    print(x, end=' ')
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)