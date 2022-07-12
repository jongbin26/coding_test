import sys
sys.setrecursionlimit(15000)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

low = min(map(min, graph))    
high = max(map(max, graph))  #2차원 리스트에서 최대값 구하는 방법!

visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y, k):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == 0 and graph[x][y] >= k:
        visited[x][y] = 1
        dfs(x-1, y, k)
        dfs(x+1, y, k)
        dfs(x, y-1, k)
        dfs(x, y+1, k)
        return True
    return False

safeArea = []
global total
total = 0

for k in range(low, high+1):
    for i in range(n):
    	for j in range(n):
            if dfs(i, j, k) == True:
                total += 1
    safeArea.append(total)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    total = 0
        
print(max(safeArea))