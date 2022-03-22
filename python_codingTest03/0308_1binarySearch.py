#이진(이분)탐색
#단계마다 범위를 반으로 나누기에 연산횟수는 logN에 비례!!

# 떡 자르기

n,m = list(map(int,input().split()))
arr= list(map(int,input().split()))

start=0
end=max(arr)

res=0
while start <= end :
    total=0
    mid=(start + end)//2
    for i in arr:
        if i > mid:
            total += i - mid
    if total <m:
        end=mid-1
    else:
        res = mid
        start = mid +1

print(res)