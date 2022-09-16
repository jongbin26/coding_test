N = int(input())
K = int(input())
dist = (list(map(int, input().split())))
dist.sort()

minus = []
for i in range(0, N-1):
    minus.append(dist[i+1]-dist[i])
minus.sort()
minus = minus[0:len(minus)-(K-1)]
print(sum(minus))