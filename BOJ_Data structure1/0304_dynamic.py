# 17404 RGB거리 2 : rgb거리문제+ 첫번째집과 마지막집의 색이 달라야함

# rgb거리 문제 풀이:
# n개의 집 중에 2개씩 모든 경우를 구해보면
# n번째 집이 red일때 = n번째 집의 red비용+ (n-1집의 g비용 or n-1집의 b비용)
# 이때 점화식 dp[i][0]=     dp[i][0]   + min( dp[i-1][1] , dp[i-1][2] ) 
# green, blue일때도 이런식으로 점화식 도출

import sys

n=int(input())
costs=[]
for _ in range(n):
    costs.append(list(map(int,input().split())))
dp= [ [0]*3 for _ in range(n)]

res=sys.maxsize # 그냥 엄청 큰 수

for first in range(3): # 첫번째 집의 색
    
    for i in range(3): # 첫번째 집의 색을 강제로 지정
        if first ==i:
            dp[0][i] = costs[0][i]
        else:
            dp[0][i] = res # 두번째 집의 색이 첫번째 색과 다르도록함(이값들이 커야 아래 for문에서 두번째집이 dp[i][0]이 안됨)
    
    for i in range(1,n): # 두번째 집부터 마지막 집 까지 경우 
        dp[i][0] = costs[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = costs[i][1]+min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = costs[i][2]+min(dp[i-1][0],dp[i-1][1])
    
    for i in range(3): # 마지막집의 색 지정
        if first == i: 
            continue
        else:           # 첫번째집과 마지막집의 색이 다르도록
            res= min(res,dp[n-1][i])
print(res)
