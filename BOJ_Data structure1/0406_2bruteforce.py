# 9095 1,2,3 더하기
# '15990 :1,2,3 더하기 5 : 같은 수 중복사용X' 과 유사한 문제

tc=int(input())
t=[]
for _ in range(tc):
    t.append(int(input()))

dp=[0,1,2,4]+[0]*(12-4)

for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in t:
    print(dp[i])


