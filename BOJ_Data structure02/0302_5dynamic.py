#1309 동물원
# dp[n][0]:마지막 두칸 중 사자가 왼쪽에 있을 때
# dp[n][1]:                     오른쪽
# dp[n][2]:                     둘다 없을 때

n=int(input())
dp=[[0]*3 for _ in range(100001)]
mod = 9901
for i in range(3):
    dp[1][i]=1  # n=1일때
for i in range(2,100001):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%mod
    dp[i][1] = (dp[i-1][0]+dp[i-1][2])%mod
    dp[i][2] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%mod
print(sum(dp[n])%mod)
