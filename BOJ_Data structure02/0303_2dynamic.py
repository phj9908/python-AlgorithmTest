#2156 : 포도주 시식

n= int(input())
p=[0]*(10001) # n의 최대값 까지 만들어 놓기!!!!******
dp=[0]*(10001)

for i in range(1,n+1):
    p[i]=int(input())
dp[1]=p[1]
dp[2]=max(p[1],p[2],p[1]+p[2])

for i in range(3,n+1):
    dp[i]=max(dp[i-2]+p[i],dp[i-3]+p[i]+p[i-1],dp[i-1])
print(max(dp))
    
