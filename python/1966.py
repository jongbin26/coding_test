from collections import deque
t = int(input())
res = []
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idx = m
    ans = 0
    while(True):
        if queue[0] < max(queue):
            if idx == 0:
                idx = len(queue) - 1
            else:
                idx -= 1
            temp = queue.popleft()
            queue.append(temp)
        else:
            if idx == 0:
                ans += 1
                break
            else:
                queue.popleft()
                ans += 1
                idx -= 1
    
    res.append(ans)
for i in res:
    print(i)