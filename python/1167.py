n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    temp = list(map(int,input().split()))
    for i in range(1, len(temp)-1, 2):
        graph[temp[0]].append([temp[i], temp[i+1]])
def dfs(x, dist):
    for i in graph[x]:
        v, wei = i
        if distance[v] == -1:
            distance[v] = dist + wei
            dfs(v, dist+wei)

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)
long_v = distance.index(max(distance))
distance = [-1] * (n+1)
distance[long_v] = 0
dfs(long_v, 0)
print(max(distance))
