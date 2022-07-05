from collections import deque
n = int(input())
x, y = map(int, input().split())
e = int(input())

graph = [[0]* (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1

def bfs():
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        v = queue.popleft()
        for i in range (n+1):
            if graph[v][i]!=0 and visited[i]==0:
                queue.append(i)
                visited[i] = 1
                for j in range (n+1):
                    if graph[i][j]!=0:
                        graph[i][j]=graph[v][i]+1
                        
                if i==y:
                    return graph[v][i]
                
    return -1

print(bfs())
            
    
        
