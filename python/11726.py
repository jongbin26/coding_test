n = int(input())
case = [0] * (n+1)
    
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()
else:
    case[1] = 1
    case[2] = 2
    for i in range(3, n+1):
        case[i] = case[i-2] + case[i-1]
    print(case[n]%10007)