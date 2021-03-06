#2225 합분해
#https://it-garden.tistory.com/341
#dp[n][k] = dp[n-1][k]+dp[n][k-1]

n,k = map(int,input().split())
dp=[[0]*(k+1) for _ in range(n+1)] # [0+(20을 4개로 나눈것)] + [1+(19를 4개로 나눈것)] + ... + [19+(1을 4개로 나눈것)] + [20+(0을 4개로 나눈것)]
dp[0][0] =1 # 0을 나타내는 경우의 수는 0하나 뿐

for i in range(0,n+1):
    for j in range(1,k+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(dp[n][k]%1000000000)