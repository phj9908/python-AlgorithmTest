#1912 : 연속합
n=int(input())
dp=list(map(int,input().split()))
for i in range(1,len(dp)):
    dp[i] = max(dp[i],dp[i]+dp[i-1])
print(max(dp))