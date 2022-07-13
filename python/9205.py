import sys
sys.setrecursionlimit(15000)
from collections import deque

def search():
    queue = deque()
    queue.append(graph[0])
    visited[0] = True
    
    while queue:
        x = queue.popleft()
        for i in range(len(graph)):
            if graph[i] != x and abs(x[0]-graph[i][0])+abs(x[1]-graph[i][1]) <= 1000 and visited[i] == False:
                queue.append(graph[i])
                visited[i] = True
                
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    graph = []
    visited = [0] * (n+2)
    
    for _ in range(n+2):
        graph.append(list(map(int, input().split())))
    
    search()
    
    if visited[n+1] == True:
        ans.append('happy')
    else:
        ans.append('sad')
    
for i in ans:
    print(i)