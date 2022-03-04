#11054 가장 긴 바이토닉 부분 수열 : 수열 내에 오름차순 정렬, 내립차순 정렬이 있다
# 유형 1:{10, 20, 30, 25, 20} : 어떤 수(30)를 기준으로 오름차순, 내림차순 둘 다 존재
# 유형 2:{10, 20, 30, 40} :어떤 수(40)을 기준으로 오름차순 정렬
# 유형 3:{50, 40, 30, 10} : 어떤 수 (50)을 기준으로 내림차순 정렬
# 가장 긴 증가하는 부분 수열 + 가장 긴 감소하는 부분 수열 문제!

n= int(input())
p=list(map(int,input().split()))
increase_dp=[1 for _ in range(n)]
decrease_dp=[1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if p[i] > p[j] :
            increase_dp[i]=max(increase_dp[i],increase_dp[j]+1)

for i in range(n-1,-1,-1):  # 가장 긴 감소하는 부분 수열은 입력받은 수열을 역방향으로 돌려서 구하기
    for j in range(n-1,i,-1):
        if p[i] > p[j]:
            decrease_dp[i] = max(decrease_dp[i],decrease_dp[j]+1)

res=[0]*n
for i in range(n):
    res[i] = increase_dp[i]+decrease_dp[i]-1 # -1: 1 2 4 5 3 2 이면  1 2 3 4 5 / 5 3 2이때 중복되는 5 하나 빼기

print(max(res))

