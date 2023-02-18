import copy
n = int(input())
temp = list(map(int, input()))
after = list(map(int, input()))

def rotate(first_bool):
    before = copy.deepcopy(temp)
    if first_bool:
        count = 1
        before[0], before[1] = not before[0], not before[1]
        if before == after:
            print(count)
            exit()
    else:
        count = 0
        if before == after:
            print(count)
            exit()
    for i in range(1, n):
        if before[i-1] != after[i-1]:
            count += 1
            if i == n-1:
                before[i-1], before[i] = not before[i-1], not before[i]
            else:
                before[i-1], before[i], before[i+1] = not before[i-1], not before[i], not before[i+1]
    if before == after:
        return count
    else:
        return -1

ans = []
ans.append(rotate(1))
ans.append(rotate(0))
if ans[0] >= 0 and ans[1] >= 0 and ans[0] <= ans[1]:
    print(ans[0])
elif ans[0] >= 0 and ans[1] >= 0 and ans[0] >= ans[1]:
    print(ans[1])
elif ans[0] >= 0 and ans[1] < 0:
    print(ans[0])
elif ans[1] >= 0 and ans[0] < 0:
    print(ans[1])
else:
    print(-1)