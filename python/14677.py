from collections import deque
import copy
n = int(input())
tablet = deque(list(input()))

template = {
    'B' : 'L',
    'L' : 'D',
    'D' : 'B'
}
ans = 0
visited = [[0] * (n * 3) for _ in range(n * 3)]
def bfs():
    global ans, tablet
    queue = deque()
    if tablet and tablet[0] == 'B':
        new_tablet = copy.deepcopy(tablet)
        new_tablet.popleft()
        queue.append((template['B'], new_tablet, 1, 1, n*3 - 1))
    if tablet and tablet[-1] == 'B':
        new_tablet = copy.deepcopy(tablet)
        new_tablet.pop()
        queue.append((template['B'], new_tablet, 1, 0, n*3 - 1 - 1))
    while queue:
        now, tablet, len, start, end = queue.popleft()
        ans = max(ans, len)
        if start + 1 <= n * 3 - 1:
            if not visited[start+1][end] and tablet and tablet[0] == now:
                new_tablet = copy.deepcopy(tablet)
                new_tablet.popleft()
                visited[start+1][end] = True
                queue.append((template[now], new_tablet, len + 1, start+1, end))
        if end - 1 >= 0:
            if not visited[start][end-1] and tablet and tablet[-1] == now:
                new_tablet = copy.deepcopy(tablet)
                new_tablet.pop()
                visited[start][end-1] = True
                queue.append((template[now], new_tablet, len + 1, start, end-1))
bfs()
print(ans)