# 3307. 최장 증가 부분 수열
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    print(f'#{t} {max(dp)}')