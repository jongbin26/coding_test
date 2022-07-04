n = int(input())
graph = []
sizeList=[]
global size
size = 0
total = 0

for _ in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x, y):
    global size
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        size+=1
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return size
    return False

for i in range(n):
    for j in range(n):
        k = dfs(i, j)
        if k != False:
            sizeList.append(k)
            total+=1
            size = 0
            
sizeList.sort()
print(total)
for i in sizeList:
    print(i)
