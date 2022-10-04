n = int(input())
ans = []
for _ in range(n):
    num = int(input())
    zero = [0] * (num + 1)
    one = [0] * (num + 1)
    
    if num == 0:
        ans.append([1, 0])
    elif num == 1:
        ans.append([0, 1])
    else:
        zero[0], zero[1] = 1, 0
        one[0], one[1] = 0, 1
        for i in range(2, num+1):
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
        ans.append([zero[num], one[num]])
for i in ans:
    print(i[0], i[1])