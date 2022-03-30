#11055 가장 큰 증가 부분 수열의 합
n=int(input())
dp=[0]*n
p=list(map(int,input().split()))
dp[0]=p[0]

for i in range(1,n): 
    for j in range(i) :
        if p[i] > p[j]:
            dp[i]=max(dp[i],dp[j]+p[i])
        else :
            dp[i]=max(dp[i],p[i]) # 지금까지의 dp값 혹은 자기자신 할당
print(max(dp))
