#1932 정수 삼각형
n=int(input())
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

k=2 # 두번째 줄 부터 연산 시작하기
for i in range(1,n):
    for j in range(k):
        if j==0:    # 줄의 첫번째 항, 자기 바로위 숫자 더하기
            dp[i][j] +=dp[i-1][j]
        elif j==i:  # 줄의 마지막 항 , 위와 동일
            dp[i][j] +=dp[i-1][j-1]
        else:
            dp[i][j] +=max(dp[i-1][j-1],dp[i-1][j]) # 왼쪽 위 숫자와 오른쪽 위 숫자 중 더 큰 값 더하기
    k+=1
print(max(dp[n-1]))