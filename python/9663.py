n = int(input())
graph = [0] * n
ans = 0

def check(x):
    for i in range(x):
        if (graph[x] == graph[i] or (x - i) == abs(graph[x] - graph[i])):
            return 0
    return 1

def nqueen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        graph[x] = i
        if check(x):
            nqueen(x + 1)
            
nqueen(0)
print(ans)