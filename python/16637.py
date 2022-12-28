from collections import deque
n = int(input())
k = input()
if n == 1:
    print(k)
    exit()
elif n == 3:
    print(eval(k))
    exit()
arr = [0] * (2*n+1)
oper = ['+', '-', '*']
for i in range(2*n+1):
    if i % 2 == 0:
        arr[i] = ''
    else:
        arr[i] = str(k[i//2])
def dfs(i):
    global ans
    if i <= 2*n:
        if i % 4 == 0 and i+6 <= 2*n:
            arr[i] = '('
            arr[i+6] = ')'
            dfs(i+6)
            arr[i] = ''
            arr[i+6] = ''
        dfs(i+2)
    else:
        ans = max(ans, int(calc(change(''.join(arr)))))
        return
def change(x):
    i = 0
    temp = ''
    while(i < len(x)):
        if x[i] == '(':
            temp += str(eval(x[i+1:i+4]))
            i += 5
        else:
            temp += x[i]
            i += 1
    return temp
def toList(x):
    res = []
    i = 0
    temp = ''
    while(i < len(x)):
        if x[i] in oper:
            res.append(x[i])
            i += 1
        else:
            while(i < len(x) and x[i] not in oper):
                temp += x[i]
                i += 1
            res.append(temp)
            temp = ''
    return res

def calc(x):
    queue = deque(toList(x))
    temp = ''
    while(len(queue) != 1):
        pop = queue.popleft()
        if pop in oper:
            temp += pop
            temp += queue.popleft()
            temp += queue.popleft()
            pop = queue.popleft()
            if pop in oper:
                temp += pop
                temp += queue.popleft()
            else:
                temp += pop
        else:
            temp += pop
            temp += queue.popleft()
            pop = queue.popleft()
            if pop in oper:
                temp += pop
                temp += queue.popleft()
            else:
                temp += pop
        queue.appendleft(str(eval(temp)))
        temp = ''
    return (queue[0])
ans = -int(1e9)
dfs(0)
print(ans)