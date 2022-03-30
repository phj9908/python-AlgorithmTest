#1149 rgb거리(각각의 집 사이 비용 최소값 구하기)# 다시 풀어보기
#https://zidarn87.tistory.com/272

# n개의 집 중에 2개씩 모든 경우를 구해보면
# n번째 집이 red일때 = n번째 집의 red비용+ (n-1집의 g비용 or n-1집의 b비용)
# 이때 점화식 dp[i][0]=     dp[i][0]   + min( dp[i-1][1] , dp[i-1][2] )
# n번째 집이 green일때 = n번째 집의 green비용+(n-1집의 r비용+ n-1집의 b비용)
#            dp[i][1] =     dp[i][1]   + min( dp[i-1][0] , dp[i-1][2] )  
# blue일때도 이런식으로 점화식 도출

n=int(input())
dp=[]

for i in range(n):
    dp.append(list(map(int,input().split()))) # 이차원 리스트로 생성
for i in range(1,n): # dp[0][0]~dp[0][2]는 입력값 그대로
    dp[i][0]+= min(dp[i-1][1],dp[i-1][2])
    dp[i][1]+= min(dp[i-1][0],dp[i-1][2])
    dp[i][2]+= min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))