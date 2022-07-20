#입력 부분
import copy
from itertools import combinations
n, k = map(int, input().split())
words = []
union = []
word_set = [[]for _ in range(n)]
for _ in range(n):
    words.append(input())

for idx, word in enumerate(words):
    for char in word:
        if char not in ('a', 'n', 'c', 't', 'i'):
        	word_set[idx].append(char)
    union = list(set(union)|set(word_set[idx]))

#여기부터 문제 시작
ans = 0
if k < 5:
    print(0)
    exit()
else:
    if k - 5 <= 1:
        combi = union
    else:
        combi = list(combinations(union,k-5))
    
    #각각의 조합
    for i in range(len(combi)):
        tmp_max = 0
        tmp = copy.deepcopy(word_set)
        # print(word_set)
        for word in tmp:
            for j in range(k-5):
                if combi[i][j] in word:
                    word.remove(combi[i][j])
        for i in tmp:
            if not i:
                tmp_max += 1
        ans = max(ans, tmp_max)
    print(ans)
        
        