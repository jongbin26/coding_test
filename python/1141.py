n = int(input())
head = [input() for _ in range(n)]
head.sort(key = lambda x : len(x), reverse=True)
ans = []
for i in range(len(head)):
    is_contained = False
    for j in range(i-1, -1, -1):
        if head[i] == head[j][:len(head[i])]:
            is_contained = True
    if not is_contained:
        ans.append(head[i])
print(len(ans))