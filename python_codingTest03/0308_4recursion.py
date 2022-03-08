# 이분탐색을 재귀함수로 표현

arr=[]
for _ in range(4): # 랜선 길이입력
    arr.append(int(input()))

start=0
end=max(arr)
res=0


def recursion(arr,start,end):
    
    if start > end :
        return -1
    mid = (start+end)//2
    sum=0
    for i in arr:
        sum += i//mid

    if sum>10:    
        return recursion(arr,mid+1,end)
    elif sum<10:
        return recursion(arr,start,mid-1)
    else:
        return mid

print(recursion(arr,start,end))