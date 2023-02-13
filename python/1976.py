n = int(input())
m = int(input())
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
        
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)
route = list(map(int, input().split()))
temp = find_parent(parent, route[0])
for i in route:
    if find_parent(parent, i) != temp:
        print("NO")
        exit(0)
print("YES")