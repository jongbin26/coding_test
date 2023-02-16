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
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
know = list(map(int, input().split()))
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split())))
for party in parties:
    num = party[0]
    party = party[1:]
    for i in range(len(party)-1):
        union(parent, party[i], party[i+1])
ans = m
for party in parties:
    party = party[1:]
    party_bool = False
    for i in party:
        if party_bool: break
        for j in know[1:]:
            if find(parent, i) == find(parent, j):
                ans -= 1
                party_bool = True
                break
print(ans)