# 안테나 (수정하기)
n=int(input())
arr=[0]+sorted(list(map(int,input().split())))
answer=[]

for i in range(1,len(arr)):
    tmp=0
    for j in range(1,len(arr)):
        tmp+=abs(arr[j]-arr[i])
    answer.append([tmp,i])
answer=sorted(answer,key=lambda x:x[0])
print(arr[answer[0][1]])
    