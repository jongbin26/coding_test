import itertools
from collections import deque
n = int(input())
virus = [input() for _ in range(n)]
permutations = list(itertools.permutations(virus, n))
ans = 1e9
for permutation in permutations:
    queue = deque(permutation)
    while len(queue) > 1:
        a = queue.popleft()
        b = queue.popleft()
        length = min(len(a), len(b))
        flag = True
        for i in range(length, -1, -1):
            if a[-i:] == b[:i]:
                flag = False
                queue.appendleft(a + b[i:])
                break
        if flag:
            queue.appendleft(a+b)
    ans = min(ans, len(queue[0]))
print(ans)