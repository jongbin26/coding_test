t = int(input())
trees = []
ans = []
for x in range(t):
    n = int(input())
    tree = list(map(int, input().split()))
    trees.append(tree)
    trees[x].sort(reverse= True)
    level = 0
    for i in range(0, len(trees[x])-2):
        level_tmp = max(trees[x][i]-trees[x][i+1], trees[x][i]-trees[x][i+2])
        level = max(level, level_tmp)
    ans.append(level)
    
for i in ans:
    print(i)