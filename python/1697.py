
from collections import deque
n, k = map(int, input().split())

visited = []
def bfs(n):
    queue = deque()
    queue.append(n)
    tmp[n] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            print(tmp[x])
            break
        a = x+1  #6
        b = x-1	 #4
        c = 2*x  #10
            
        if 0<=a<MAX:
            if tmp[a]==0:
                queue.append(a)
                tmp[a] = tmp[x] + 1
        if 0<=b<MAX:
            if tmp[b]==0:
                queue.append(b)
                tmp[b] = tmp[x] + 1
        if 0<=c<MAX:
            if tmp[c]==0:
                queue.append(c)
                tmp[c] = tmp[x] + 1
        
MAX = 10 ** 5
tmp = [0] * (MAX+1)

bfs(n)