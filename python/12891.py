s, p = map(int, input().split())
string = input()
a, c, g, t = map(int, input().split())

ans=0
temp = string[0:p]
count =[temp.count('A'), temp.count('T'), temp.count('G'), temp.count('C')]
if count[0] >= a and count[1] >= t and count[2] >= g and count[3] >= c:
    ans += 1
for i in range(1, s-p+1):
    #이전값
    if string[i-1] == 'A':
        count[0] -= 1
    elif string[i-1] == 'T':
        count[1] -= 1
    elif string[i-1] == 'G':
        count[2] -= 1
    else:
        count[3] -= 1
    #다음값
    if string[i+p-1] == 'A':
        count[0] += 1
    elif string[i+p-1] == 'T':
        count[1] += 1
    elif string[i+p-1] == 'G':
        count[2] += 1
    else:
        count[3] += 1
    #비교
    if count[0] >= a and count[1] >= t and count[2] >= g and count[3] >= c:
        ans += 1

print(ans)