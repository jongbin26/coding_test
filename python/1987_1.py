r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
visited = [0] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[ord(graph[nx][ny])-ord('A')]:
                visited[ord(graph[nx][ny])-ord('A')] = 1
                dfs(nx, ny, cnt+1)
                visited[ord(graph[nx][ny])-ord('A')] = 0
    return
visited[ord(graph[0][0])-ord('A')] = 1
ans = 0
dfs(0, 0, 1)
print(ans)