n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
visited[graph[0][0]][0], visited[0][graph[0][0]] = 1, 1

ans = 0
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if visited[i][j] > 0:
            move = graph[i][j]
            if i + move < n:
                visited[i + move][j] += visited[i][j]
            if j + move < n:
                visited[i][j + move] += visited[i][j]
print(visited[n-1][n-1])