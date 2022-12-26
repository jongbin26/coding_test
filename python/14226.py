from collections import deque
s = int(input())
visited = [[0] * (s+1) for _ in range(s+1)]
def bfs():
    queue = deque()
    queue.append((0, 1, 0))
    while(queue):
        cnt, screen, clipboard  = queue.popleft()
        if screen == s:
            return cnt
        if not visited[screen][screen]:
            visited[screen][screen] = True
            queue.append((cnt+1, screen, screen))
        if clipboard and screen + clipboard <= s and not visited[screen+clipboard][clipboard]:
            visited[screen+clipboard][clipboard] = True
            queue.append((cnt+1, screen + clipboard, clipboard))
        if screen-1 >= 0 and not visited[screen-1][clipboard]:
            visited[screen-1][clipboard] = True
            queue.append((cnt+1, screen-1, clipboard))       
print(bfs())