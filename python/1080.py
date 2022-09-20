N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input())))
for _ in range(N):
    B.append(list(map(int, input())))

def turn(graph, a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            if graph[i][j] == 1:
                graph[i][j] = 0
            else:
                graph[i][j] = 1

ans = 0
for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            turn(B, i, j)
            ans += 1

if(N < 3 or M < 3):
    if (A == B):
        print(0)
        exit()
    else:
        print(-1)
        exit()

if (A == B):
    print(ans)
else:
    print(-1)