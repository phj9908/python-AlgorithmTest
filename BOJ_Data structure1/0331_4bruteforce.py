# 9095 1,2,3 더하기
tc=int(input())

dp=[0,1,2,4]+[0]*(12-4)
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in range(tc):
    n=int(input())
    print(dp[n[i]])