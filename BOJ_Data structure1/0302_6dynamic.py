#11057 오르막수 2234, 3678 -> O / 2232, 8111 -> X
# 길이가 1인 오르막수의 갯수 10 (0~9)
# 길이가 3이고 2로 시작하는 오르막수 갯수 -> dp[3][2]

n= int(input())
dp=[[0]*10 for _ in range(n+1)]
mod=10007
for i in range(10):
    dp[1][i]=1
for i in range(2,n+1):
    for j in range(10):
        for k in range(j,10):
            dp[i][j]+=dp[i-1][k]

print(sum(dp[n])%mod)

