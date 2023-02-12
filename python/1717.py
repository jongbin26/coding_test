import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
#parent initialization
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

ans = []
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            ans.append("YES")
        else:
            ans.append("NO")
for i in ans:
    print(i) 