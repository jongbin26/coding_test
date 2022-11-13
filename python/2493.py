n = int(input())
temp = list(map(int, input().split()))
tower = []
for i in range(len(temp)):
    tower.append([i, temp[i]])

stack = []
ans = [0] * n
for i in range(0, len(tower)):
    while(True):
        if stack:
            if stack[-1][1] < tower[i][1]:
                stack.pop()
            else:
                ans[i] = stack[-1][0] + 1
                stack.append([tower[i][0], tower[i][1]])
                break
        else:
            ans[i] = 0
            stack.append([tower[i][0], tower[i][1]])
            break
for i in ans:
    print(i, end=' ')