from collections import deque
n = int(input())
ans = []
queue = deque()
for _ in range(n):
    word = list(input().split())
    if word[0] == 'push_front':
        queue.appendleft(word[1])
    if word[0] == 'push_back':
        queue.append(word[1])
    if word[0] == 'pop_front':
        ans.append(queue.popleft()) if queue else ans.append(-1)
    if word[0] == 'pop_back':
        ans.append(queue.pop()) if queue else ans.append(-1)
    if word[0] == 'size':
        ans.append(len(queue))
    if word[0] == 'empty':
        ans.append(0) if queue else ans.append(1)
    if word[0] == 'front':
        ans.append(queue[0]) if queue else ans.append(-1)
    if word[0] == 'back':
        ans.append(queue[-1]) if queue else ans.append(-1)
for i in ans:
    print(i)