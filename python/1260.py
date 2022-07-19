from collections import deque #for BFS 
n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1
    
def dfs(v):
    visited[v]=1
    print(v, end=' ')
    for i in range(n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)

            
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v]=1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(n+1):
            if visited[i]==0 and graph[v][i]==1:
                queue.append(i)
                visited[i]=1

visited=[0]*(n+1)           
dfs(v)

print("")

visited=[0]*(n+1)
bfs(v)