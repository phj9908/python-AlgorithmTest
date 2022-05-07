#2491 수열
n=int(input())
arr=list(map(int,input().split()))
p_dp=[1]*n
m_dp=[1]*n
for i in range(1,n):
    if arr[i-1]<=arr[i]:
        p_dp[i]=p_dp[i-1]+1
for i in range(1, n):
    if arr[i-1]>=arr[i]:
        m_dp[i]=m_dp[i-1]+1

print(max(max(p_dp),max(m_dp)))
