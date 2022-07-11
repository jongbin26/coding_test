n=int(input())
list = []
for _ in range(n):
    list.append(int(input()))
    
list.sort()
leng = len(list)

total=0
for el in list:
    total+=el
#평균값
a = round(total/leng)

#중간값
b = list[leng//2]

#최빈값
tmp=[0]*8001

for i in list:
    tmp[i+4000]+=1
maxNum = max(tmp)
maxNumList = []
for j in range(len(tmp)):
    if tmp[j] == maxNum:
        maxNumList.append(j)
        
if(len(maxNumList)>1):
    c = maxNumList[1]-4000
else:
    c = maxNumList[0]-4000

#범위
d = list[leng-1]-list[0]

answers = [a, b, c, d]

for ans in answers:
    print(ans)
    