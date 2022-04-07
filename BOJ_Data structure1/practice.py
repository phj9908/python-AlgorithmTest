n,m=map(int,input().split())

dp=[ list(map(int,input().split())) for i in range(2)]
dp[1][0]+=dp[0][0]

for i in range(1,m):
    dp[0][i]+=dp[0][i-1]
    dp[1][i]+=max(dp[1][i-1],dp[0][i])
    
print(dp[1][m-1])
