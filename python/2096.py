n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp_max = [[0] * 3 for _ in range(2)]
dp_min = [[0] * 3 for _ in range(2)]

dp_max[0][0], dp_max[0][1], dp_max[0][2] = graph[0][0], graph[0][1], graph[0][2]
dp_min[0][0], dp_min[0][1], dp_min[0][2] = graph[0][0], graph[0][1], graph[0][2]
for i in range(1, n):
    temp = i % 2
    dp_max[temp][0] = max(dp_max[temp-1][0] + graph[i][0], dp_max[temp-1][1] + graph[i][0])
    dp_max[temp][1] = max(dp_max[temp-1][0] + graph[i][1], dp_max[temp-1][1] + graph[i][1], dp_max[temp-1][2] + graph[i][1] )
    dp_max[temp][2] = max(dp_max[temp-1][1] + graph[i][2], dp_max[temp-1][2] + graph[i][2])
    
    dp_min[temp][0] = min(dp_min[temp-1][0] + graph[i][0], dp_min[temp-1][1] + graph[i][0])
    dp_min[temp][1] = min(dp_min[temp-1][0] + graph[i][1], dp_min[temp-1][1] + graph[i][1], dp_min[temp-1][2] + graph[i][1] )
    dp_min[temp][2] = min(dp_min[temp-1][1] + graph[i][2], dp_min[temp-1][2] + graph[i][2])
    
print(max(dp_max[(n-1)%2]), min(dp_min[(n-1)%2]))    