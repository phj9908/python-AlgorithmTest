#11726 2 x n타일링 1x2,2x1타일로 채우는 방법의 수
#n=1일때 방법의수 1개, n=2일때 2개, n=3일때 3, 4일때 5,5일 때 8
# 점화식 dp[n]= dp[n-2]+dp[n-1] (n개에서 타일을 채울수있는 방법의 수)
# n-2는 누워있는 타일2개 / n-1은 세워진 타일 하나를 뜻함

n= int(input())
dp=[0,1,2]+([0]*(1001-3))

for i in range(3,1001):
    dp[i]=dp[i-2]+dp[i-1]
    
print(dp[n]%10007)
