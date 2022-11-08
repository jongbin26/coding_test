T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    book = [input() for _ in range(n)]
    book.sort()
    
    consistancy = True
    
    for i in range(len(book)-1):
        if book[i] == book[i+1][:len(book[i])]:
            consistancy = False
    if consistancy:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)