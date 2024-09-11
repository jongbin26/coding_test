import sys
sys.setrecursionlimit(5000)
n, m = map(int ,input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
ans = 0
for a, b, c in edges:
    if not (find(parent[a]) == find(parent[b])):
        union(a, b)
        ans += c
print(ans)