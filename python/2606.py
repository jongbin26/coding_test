from collections import deque
n = int(input())
v = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(v):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited = [0] * (n+1)

global total
total=0

def dfs(v):
    visited[v] = 1
    global total
    # print(total, end =' ')
    for i in range(n+1):
        if graph[v][i]==1 and visited[i] == 0:
            total+=1
            dfs(i)
    return total

print(dfs(1))
#save