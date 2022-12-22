T = int(input())      
calc = ['+', '-', ' ']
def dfs(oper, cnt):
    global temp_ans
    if len(oper) == 2 * n - 1:
        if eval(oper.replace(" ","")) == 0:
            temp_ans.append(oper)
        return
    for i in calc:
        oper+=i
        oper+=str(cnt+1)
        dfs(oper, cnt+1)
        oper = oper[:-2]
ans = []
for _ in range(T):
    n = int(input())
    temp_ans = []
    dfs("1", 1)
    temp_ans.sort()
    for i in temp_ans:
        ans.append(i)
    ans.append("")
for i in range(0, len(ans)-1):
    print(ans[i])