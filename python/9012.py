from collections import deque
n = int(input())
def check(string):
    queue = deque()
    for char in string:
        if char == ')':
            while(True):
                if queue:
                    temp = queue.pop()
                    if temp == '(':
                        break
                else:
                    return 'NO'
        else:
            queue.append(char)
    if queue:
        return 'NO'
    else:
        return 'YES'

ans = []
for _ in range(n):
    string = input()
    ans.append(check(string))
for i in ans:
    print(i)