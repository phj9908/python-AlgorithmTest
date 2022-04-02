#15988 1,2,3더하기 3:
# 9095번과 유사.
import sys

dp=[0,1,2,4]+[0]*(1000001-4)

mod=1000000009
for i in range(4,1000001):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%mod

t= int(input())
for _ in range(t):
    n=int(sys.stdin.readline())
    print(dp[n]%mod)