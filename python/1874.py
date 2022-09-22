N = int(input())
stack = []
answer = []
ans_bool = False
tmp = 1
for i in range(N):
    num = int(input())
    while tmp <= num:
        stack.append(tmp)
        answer.append('+')
        tmp += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        ans_bool = True
        break
        
if ans_bool == False:
    for i in answer:
        print(i)