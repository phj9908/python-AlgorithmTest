#9095:정수 n을 1,2,3더하기로 나타내는 방법의 수
# ex) 4 나타내기 : 1+3 =1+dp[3], 2+2= 2+dp[2] ...
t=int(input())
dp=[0,1,2,4]+([0]*(12-4))
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(t):
    n=int(input())
    print(dp[n])

