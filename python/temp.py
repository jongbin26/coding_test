from collections import deque

n = int(input())

def d(num):
    num = int(num)
    num *= 2
    num %= 10000
    temp = '0' * (4-len(str(num)))
    return temp + str(num)

def s(num):
    num = int(num)
    if num == 0:
        return '9999'
    else:
        num -= 1
        temp = '0' * (4-len(str(num)))
        return temp + str(num)

def l(num):
    return (num[1] + num[2] + num[3] + num[0])

def r(num):
    return (num[3] + num[0] + num[1] + num[2])

def bfs(oper):
    global res
    queue = deque()
    temp = '0' * (4-len(str(oper)))
    oper = temp + str(oper)
    queue.append((oper, ''))
    while queue:
        oper, ans = queue.popleft()
        if oper == str(b):
            return ans
        if not visited[int(d(oper))]:
            visited[int(d(oper))] = 1
            queue.append((d(oper), ans+'D'))

        if not visited[int(s(oper))]:
            visited[int(s(oper))] = 1
            queue.append((s(oper), ans+'S'))

        if not visited[int(l(oper))]:
            visited[int(l(oper))] = 1
            queue.append((l(oper), ans+'L'))

        if not visited[int(r(oper))]:
            visited[int(r(oper))] = 1
            queue.append((r(oper), ans+'R'))

res = []
for _ in range(n):
    a, b = map(int, input().split())
    temp = '0' * (4-len(str(b)))
    b = temp + str(b)
    visited = [0] * 10000
    res.append(bfs(str(a)))
for i in res:
    print(i)