from collections import deque
K = int(input())
ans = []
for _ in range(K):
    min_ans = int(1e9)
    max_ans = 0
    w = input()
    k = int(input())
    alpha = [deque() for _ in range(26)]
    for i in range(len(w)):
        alpha[ord(w[i]) - ord('a')].append(i)
        if len(alpha[ord(w[i]) - ord('a')]) == k:
            min_ans = min(min_ans, alpha[ord(w[i]) - ord('a')][k-1] - alpha[ord(w[i]) - ord('a')][0])
            max_ans = max(max_ans, alpha[ord(w[i]) - ord('a')][k-1] - alpha[ord(w[i]) - ord('a')][0])
            alpha[ord(w[i]) - ord('a')].popleft()
    if min_ans == int(1e9) and max_ans == 0:
        ans.append(-1)
    else:
        ans.append([min_ans + 1, max_ans + 1])
for i in ans:
    if i != -1:
        print(i[0], i[1])
    else:
        print(i)