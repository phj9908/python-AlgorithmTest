# 1699:제곱수의 합
import sys

n=int(sys.stdin.readline())
dp=[i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,int(i**0.5)+1):
        if i<j*j:
            break
        if dp[i] > 1+dp[i-j*j]: # = dp[j*j]+dp[i-j*j]
            dp[i]=1+dp[i-j*j]
print(dp[n])