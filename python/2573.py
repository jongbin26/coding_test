import sys
sys.setrecursionlimit(15000)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] != 0 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

def newGraph(graph):
    minus = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if graph[i-1][j] == 0:
                    count += 1
                if graph[i+1][j] == 0:
                    count += 1
                if graph[i][j-1] == 0:
                    count += 1
                if graph[i][j+1] == 0:
                    count += 1
                minus[i][j] = count
                count = 0
    for i in range(n):
        for j in range(m):
            tmp = graph[i][j] - minus[i][j]
            if tmp <= 0:
                graph[i][j] = 0
            else: graph[i][j] = tmp
    
    return graph

time = 0
area = 0

while(time >= 0):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                area += 1
    
    if area >= 2:
        print(time)
        break
    
    if max(map(max, graph))==0:
        print(0)
        break
    #그래프 변경
    time += 1
    graph = newGraph(graph)
    area = 0