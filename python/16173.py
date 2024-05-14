n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if graph[x][y] == -1:
        return True
    if visited[x][y]:
        return False
    visited[x][y] = True
    
    jump = graph[x][y]
    if y + jump < n:
        if dfs(x, y + jump):
            return True
    if x + jump < n:
        if dfs(x + jump, y):
            return True
    
    return False

print("HaruHaru" if dfs(0, 0) else "Hing")