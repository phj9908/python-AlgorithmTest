#11722 가장 긴 감소하는 부분 수열
# 이 방법외에 for(n-1,-1,-1)로 역방향으로 바꿔서 가장긴 증가하느 부분 구하는 방법이랑 동일하게 해도 됨
n= int(input())
p=list(map(int,input().split()))
dp=[1]*(n+1)
for i in range(1,n):
    for j in range(i):
        if p[i] < p[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
