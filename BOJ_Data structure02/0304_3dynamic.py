#13398 연속합2
# 수열에서 하나의 수를 제거할 수 있을때(필수는 아님) 최대 합?
# 본인이나 그 이전 수를 제외하고 더하거나 (제거할 횟수가 남아있지않음)-> dp[0][i] 
#                둘다 포함하고          (              남아있음)  -> dp[1][i]
n=int(input())
p=list(map(int,input().split()))
dp=[[0]*n for _ in range(2)]
dp[0][0],dp[1][0] = p[0],p[0]

for i in range(1,n):
    dp[0][i] = max(dp[1][i-1],dp[0][i-1] +p[i]) # 본인을제외하고  그이전까지 더하기, 그이전수를 제외하고 본인더하기
    dp[1][i] = max(dp[1][i-1]+p[i],p[i])

max=dp[0][0]
for i in range(2):
    for j in range(n):
        if max < dp[i][j]:
            max=dp[i][j]
print(max)