S = input()
T = input()

n = len(T)-len(S)
for i in range(n):
    if T[len(T)-1] == 'A':
        T = T[:len(T)-1]
    else:
        T = T[:len(T)-1]
        T = T[::-1]
if S == T:
    print(1)
else:
    print(0)