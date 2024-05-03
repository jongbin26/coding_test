from collections import deque

num_pc = int(input()) #input으로 컴퓨터의 숫자를 입력
N = int(input()) #연결된 컴퓨터 쌍
a = list()
b = list()
# queue = [1] 

graph = [[]for _ in range(num_pc + 1)]
#행의 개수가 num_pc + 1인 2차원 리스트
#그래프 간선끼리의 연결 정보를 담은 리스트 

visited = [False for _ in range(num_pc + 1)] 

for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
#입력받은 값을 바탕으로 그래프 생성

queue = deque()
queue.append(1)
visited[1] = True

while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print(visited)