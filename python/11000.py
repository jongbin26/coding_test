import heapq
N = int(input())

room = [list(map(int, input().split())) for _ in range(N)]
room.sort()

queue = []
heapq.heappush(queue, room[0][1])

for i in range(1, N):
    if room[i][0] < queue[0]:
        heapq.heappush(queue, room[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, room[i][1])

print(len(queue))