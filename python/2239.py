graph = []
for _ in range(9):
    graph.append(list(map(int, input())))
def check_line(x, y):
    temp = set([1,2,3,4,5,6,7,8,9])
    row = set(graph[x][:])
    col = set([row[y] for row in graph])
    return temp - (row | col)
def check_box(x, y):
    temp = set([1,2,3,4,5,6,7,8,9])
    x //= 3
    y //= 3
    arr = []
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if graph[i][j]:
                arr.append(graph[i][j])
    return temp - set(arr)

arr = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            arr.append([i, j])
def print_graph():
    for i in range(9):
        for j in range(9):
            print(graph[i][j], end='')
        print()
def check_ans():
    for i in range(9):
        for j in range(9):
            temp = check_line(i, j) & check_box(i, j)
            if temp:
                return False
    print_graph()
    exit()
def dfs(ptr):
    if ptr == len(arr):
        if not check_ans(): return False
    x, y = arr[ptr]
    temp = check_line(x, y) & check_box(x, y)
    for val in temp:
        graph[x][y] = val
        dfs(ptr+1)
        graph[x][y] = 0
    return False

dfs(0)