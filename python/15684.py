n, m, h = map(int, input().split())
graph = [[0] * (n) for _ in range(h)]
if m:
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
else: data = []

def check(graph):
    for i in range(n):
        locate = i
        for j in range(h):
            if graph[j][locate]:
                locate += 1
            elif locate > 0 and graph[j][locate - 1]:
                locate -= 1
        if i != locate:
            return False
    return True

ans = int(1e9)
def dfs(count, x, y):
    global ans
    if check(graph):
        ans = min(ans, count)
        return
    if count >= ans or count >= 3:
        return
    for i in range(x, h):
        temp = y if i == x else 0
        for j in range(temp, n-1):
            if not graph[i][j] and not graph[i][j+1]:
                if j > 0 and graph[i][j-1]:
                    continue
                graph[i][j] = 1
                dfs(count+1, i, j+2)
                graph[i][j] = 0

dfs(0, 0, 0)
print(ans if ans < 4 else -1)