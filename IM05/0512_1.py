# 2635 수 이어가기
n1=int(input())
n2=n1//2+1
arr=[n1,n2]
max_len=2
answer=[]
while n2<=n1:
    while 1:
        x=arr[-2]-arr[-1]
        if x<0:
            break
        arr.append(x)
    if max_len<len(arr):
        max_len=len(arr)
        answer=arr.copy()
    n2+=1
    arr=[n1,n2]
print(max_len)
print(*answer)
