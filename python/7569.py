from collections import deque

#3 dimension graph
a, b, c = map(int, input().split())
graph = [[] for _ in range(c)]

for i in range(c):
    for _ in range(b):
    	graph[i].append(list(map(int, input().split())))   
        
dx=[1, -1, 0, 0, 0, 0]
dy=[0, 0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

queue = deque()
                        
for i in range(c):
    for j in range(b):
        for k in range(a):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<a and 0<=ny<b and 0<=nz<c:
                if graph[nz][ny][nx]==0:
                	queue.append((nz, ny, nx))
                	graph[nz][ny][nx] = graph[z][y][x] + 1
 
badTomato = False
maxDay = 0
for i in range(c):
    for j in range(b):
        for k in range(a):
            maxDay = max(maxDay, graph[i][j][k])
    
for three_d in graph:
    for two_d in three_d:
        if 0 in two_d:
            badTomato = True
            
if badTomato == True:
    print(-1)
else:
    print(maxDay-1)