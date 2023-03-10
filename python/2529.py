n = int(input())
sign = input().split()
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ans = []
def dfs(depth, temp, flag):
    global num
    if depth == n:
        for i in range(flag[0], flag[1]+1):
            if num[i] == 0:
                temp += str(i)
                ans.append(temp)
                temp = temp[:-1]
        return
    for i in range(flag[0], flag[1]+1):
        if num[i] == 0:
            num[i] = 1
            temp += str(i)
            if sign[depth] == '<':
                dfs(depth+1, temp, [i+1, 9])
            elif sign[depth] == '>':
                dfs(depth+1, temp, [0, i-1])
            num[i] = 0
            temp = temp[:-1]
dfs(0, '', [0, 9])
print(ans[-1])
print(ans[0])