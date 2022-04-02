#16194 : 카드 구매하기 2
n= int(input())
card_price=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
dp[1]=card_price[1]
dp[2]=min(card_price[2],dp[1]*2)

for i in range(3,n+1):
    dp[i]=card_price[i]
    for j in range(1,i//2+1):
        dp[i]=min(dp[i],dp[i-j]+dp[j])
print(dp[n])