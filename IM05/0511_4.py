# 2635 수 이어가기
n1=int(input())
n2=n1//2+1
arr=[n1,n2]
max_len=2
answer=[]
while n2<n1:
    while 1:
        arr.append(arr[-2]-arr[-1])
        if arr[-1]<0:
            break
    if max_len<len(arr):
        max_len=len(arr)
        answer=arr.copy()
    arr[1]+=1
