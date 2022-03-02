#2193:이친수
# 문제 10844:계단수 풀이처럼 특정 자릿수의 0으로 끝날때, 1로 끝날때 를 나눠 점화식 세움
n= int(input())
dp=[[0]*2 for _  in range(91)] # range(n+1)로 하면 index err뜸
dp[1] =[0,1] # 1
dp[2] =[1,0] # 10
dp[3] = [1,1] # 100,101

for i in range(4,n+1):
    for j in range(2):
        if j==0:
            dp[i][j] = dp[i-1][1]+dp[i-1][0]
        else :
            dp[i][j] = dp[i-1][0]
print(sum(dp[n]))

#-다른 답안
# 각 자릿수의 수들을 나열하여 규칙발견
#https://pacific-ocean.tistory.com/195
# n=int(input())
# dp=[0,1,1]
# for i in range(3,91):
#     dp.append(dp[i-2]+dp[i-1])
# print(dp[n])
