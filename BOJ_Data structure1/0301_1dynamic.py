#10844 쉬운 계단수(숫자 사이 1만큼 차이나는 수 ex) 45656 )
n= int(input())
dp=[[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i]=1 # 길이가 1인 i로 끝나는 수
mod=1000000000

for i in range(2,n+1): # 210
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1] # dp[3][0]=210 ,dp[2][1]=21,
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] # dp[1][0]와dp[1][2]= 2와 1
print(sum(dp[n])%mod)