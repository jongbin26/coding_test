from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
def bfs(x):
    queue = deque()
    visited[x] = 1
    queue.append(x)
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
visited = [0] * (n+1)     
dfs(v)         
print() 
visited = [0] * (n+1)
bfs(v)