from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
def quadtree(n, x, y):
    ans = []
    if n == 1:
        ans.append(graph[x][y])
        return graph[x][y]
    
    quad = False
    #크기가 1 인 경우
    for i in range(x, (x+n)):
        for j in range(y, (y+n)):
            if graph[i][j] != graph[x][y]:
                quad = True
    if quad == True:
        ans.append(quadtree(n//2, x, y))
        ans.append(quadtree(n//2, x, (y+n//2)))
        ans.append(quadtree(n//2, (x+n//2), y))
        ans.append(quadtree(n//2, (x+n//2), (y+n//2)))
    else:
        return graph[x][y]
    return ans

ans = str(quadtree(n, 0, 0)).replace('[', '(').replace(']', ')').replace(', ', '')
print(ans)