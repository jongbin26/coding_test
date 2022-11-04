a, b = map(int, input().split())
cnt = 1
ans_bool = 0
while(b >= a):
    if a == b:
        ans_bool = 1
        break
    
    b_str = str(b)
    if b_str[len(b_str) - 1] == '1':
        b_str = b_str[:-1]
        b = int(b_str)
        cnt += 1
    elif b % 2 ==0:
        b //= 2
        cnt += 1
    else:
        break
        
    if a == b:
        ans_bool = 1
        break
        
if ans_bool:
    print(cnt)
else:
    print(-1)