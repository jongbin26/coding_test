def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)
friends = []
for i in range(1, n+1):
    friends.append((find(parent, parent[i]), cost[i-1]))
friends.sort()
now = 0
temp = 0
for friend in friends:
    if friend[0] != now:
        temp += friend[1]
        now = friend[0]
if temp <= k:
    print(temp)
else:
    print("Oh no") 