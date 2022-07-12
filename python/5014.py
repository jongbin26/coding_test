from collections import deque
f, s, g, u, d = map(int, input().split())

visited = [0] * f

def dfs():
    queue = deque()
    queue.append(s)
    visited[s-1] = 1
    while queue:
        x = queue.popleft()
        
        if x == g:
            break
            
        if x + u <= f and visited[x + u -1] == 0:
            up = x + u
            queue.append(up)
            visited[up-1] = visited[x-1] + 1
        
        if x - d >= 1 and visited[x - d -1] == 0:
            down = x - d
            queue.append(down)
            visited[down-1] = visited[x-1] + 1
            
dfs()
if visited[g-1] == 0:
    print("use the stairs")
else :
    print(visited[g-1]-1)