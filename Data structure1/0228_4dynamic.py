#11052: 카드구매하기
# n개의 카드를 구매하며 최대값을 구하기
# >> 작은 문제부터 해결하기 :: 
# dp[1]= 1개의 카드를 구매하는데 최대값: 카드 1개
# dp[2]= 2개 카드 구매하는데 최대값: 2번 카드 1개 or 1번카드 2개
# dp[3] =3개                      : 3번 카드 1개 or 1번카드 1개와 dp[2] ...
#https://pacific-ocean.tistory.com/66

n=int(input())
dp=[0]*(n+1)
card_price=[0]+list(map(int,input().split()))
dp[1]=card_price[1]
dp[2] = max(card_price[2],dp[1]*2)

for i in range(3,n+1):
    dp[i] = card_price[i] # 자기 자신으로 만드는 경우
    for j in range(1,i//2+1) : # i//2+1인 이유: i=5면 (dp[i-j],dp[j])에서 (4,1),(1,4)같은 중복 제거
            dp[i] = max(dp[i],dp[i-j]+dp[j])
print(dp[n])