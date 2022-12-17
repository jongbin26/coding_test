n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]

teacher = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
            
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def find():
    find_bool = False
    for point in teacher:
        x, y = point[0], point[1]
        for i in range(4):
            nx, ny = x, y
            while(True):
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 'S':
                        return True
                    elif graph[nx][ny] == 'O':
                        break
                else:
                    break
    return False

def dfs(cnt):
    if cnt == 3:
        if find():
            return
        else:
            print("YES")
            exit()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(cnt + 1)
                graph[i][j] = 'X'
dfs(0)
print("NO")