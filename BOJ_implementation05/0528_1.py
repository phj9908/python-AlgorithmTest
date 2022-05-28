# 18311 왕복
n,k=map(int,input().split())
arr=[0]+list(map(int,input().split()))
cnt=0
answer=-1
if k<=sum(arr):
    if k==sum(arr):
        answer=arr.index(arr[-1])
    else:
        for i in range(len(arr)-1):
            cnt+=arr[i]
            if k<cnt:
                answer=i
                break
else:
    k-=sum(arr)
    for i in range(len(arr)-1,-1,-1):
        cnt+=arr[i]
        if k<=cnt:
            answer=i
            break
print(answer)
