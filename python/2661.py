n = int(input())
arr = ''
def isGood():
    size = len(arr) // 2
    for i in range(1, size+1):
        if arr[len(arr)-i:len(arr)] == arr[len(arr)-2*i:len(arr)-i]:
            return 0
    return 1
def dfs(cnt):
    global arr
    if cnt >= 2:
        if not isGood():
            return
    if cnt == n:
        print(arr)
        exit()
    for i in range(1, 4):
        arr += str(i)
        dfs(cnt+1)
        arr = arr[:-1]
        
dfs(0)