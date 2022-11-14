l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
moeum = ['a', 'e', 'i', 'o', 'u']
ans = []
def password(temp, idx):
    if len(temp) == l:
        moeum_count = 0
        jaeum_count = 0
        for i in temp:
            if i in moeum:
                moeum_count += 1
            else:
                jaeum_count += 1
        if moeum_count >= 1 and jaeum_count >= 2:
            ans.append(''.join(temp))
        return
    for i in range(idx, len(arr)):
        temp.append(arr[i])
        password(temp, i+1)
        temp.pop()

password([], 0)
for i in ans:
    print(i)