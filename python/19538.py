from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i]= list(map(int, input().split()))[:-1]
m = int(input())
spreaders = list(map(int, input().split()))

#절반 이상이 루머 믿는지 확인 함수
def check(x, time): 
    cnt = 0
    for i in graph[x]:
        if visited[i] >= 0 and visited[i] <= time:
            cnt += 1
    if cnt >= len(graph[x])/2:
        return True
    return False

def bfs():
    queue = deque()
    for spreader in spreaders:
        visited[spreader] = 0
        queue.append((spreader, 0))
    while queue:
        x, time = queue.popleft()
        temp = deque()
        for i in graph[x]:
            #방문 안하고 절반 이상이 유포자면 temp에 저장
            if visited[i]== -1 and check(i, time):
                temp.append(i)
        #temp 돌면서 queue에 삽입
        while temp:
            k = temp.popleft()
            visited[k] = time + 1
            queue.append((k, time+1))
            
visited = [-1] * (n+1)
bfs()
print(*visited[1:])
