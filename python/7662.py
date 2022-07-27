import sys
import heapq
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    max_heap, min_heap = [], []
    visit = [False] * 1000001

    t = int(input())

    for i in range(t):
        oper, val = input().split()
        if oper == 'I':
            heapq.heappush(min_heap, (int(val), i))
            heapq.heappush(max_heap, (int(val) * -1, i))
            visit[i] = True

        elif oper == 'D':
            if val == '-1':
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif val == '1':
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')