word = list(input())
word.sort()
alpha = [0] * 26
for i in word:
    alpha[ord(i)-ord('A')] += 1
ord_cnt = 0
ans = []
temp = 0
for i in range(len(alpha)):
    if alpha[i] % 2 == 1:
        ord_cnt += 1
        temp = chr(i+ord('A'))
        for _ in range(alpha[i]//2):
            ans.append(chr(i+ord('A')))
    if ord_cnt > 1:
        print("I'm Sorry Hansoo")
        exit()
    if alpha[i] and alpha[i] % 2 == 0:
        for _ in range(alpha[i]//2):
            ans.append(chr(i+ord('A')))
if(temp):
    ans += temp
    ans += ans[:-1][::-1]
else:
    ans += ans[::-1]
print(''.join(ans))
    