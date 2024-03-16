s = input()
tag, space = False, False
idx, temp = 0, ''
ans = ''

while(idx < len(s)):
    if s[idx] == '<':
        ans += temp[::-1]
        temp = ''
        tag = True
        temp += s[idx]
    elif s[idx] == '>' and tag == True:
        tag = False
        temp += s[idx]
        ans += temp
        temp = ''
    elif s[idx] == ' ' and tag == False:
        ans += temp[::-1] + s[idx]
        temp = ''
    else:
        temp += s[idx]
    idx += 1
ans += temp[::-1]
print(ans)