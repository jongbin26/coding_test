from collections import deque
from itertools import combinations
import copy
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            home.append([i, j])
new_chicken = list(combinations(chicken, m))
ans = 100000000000
for chickens in new_chicken:
    temp_ans = 0
    for i in home:
        min_dist = 100000000000
        for j in chickens:
            min_dist = min(min_dist , abs(i[0] - j[0]) + abs(i[1] - j[1]))
        temp_ans += min_dist
    ans = min(ans, temp_ans)
print(ans)