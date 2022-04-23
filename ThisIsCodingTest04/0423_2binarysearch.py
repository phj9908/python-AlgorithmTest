# 떡볶이떡 만들기(다시풀어보기)
n,m =map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=max(arr)

while start<=end:
    mid=(start+end)//2
    total=0
    for i in arr:
        if i>mid:
            total+=i-mid
    if total<m: # 떡의 양이 부족하면
        end=mid-1
    else:       # 떡의 양이 충분하면
        answer=mid
        start=mid+1
print(answer)
