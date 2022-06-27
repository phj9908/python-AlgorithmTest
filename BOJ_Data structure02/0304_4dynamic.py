#2133 타일 채우기
# https://jyeonnyang2.tistory.com/51

n=int(input())
dp=[0]*31
dp[2]=3
for i in range(4,31,2): # n이 홀수일 땐 0
    dp[i]=dp[i-2]*dp[2]
    for j in range(4,i,2): 
        dp[i] += 2*dp[i-j]
    dp[i] +=2 # 새로운 모양 2개 추가
print(dp[n])