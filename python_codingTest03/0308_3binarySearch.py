
arr=[]
for _ in range(4): # 랜선 길이입력
    arr.append(int(input()))

start =0
end= max(arr)
res=0

while start <= end:
    sum=0
    mid=(start+end)//2
    for i in arr:
        sum+=i//mid
    if sum>10:
        start = mid+1
    elif sum<10:
        end= mid-1
    else:
        res=mid
        break
print(res)
    


