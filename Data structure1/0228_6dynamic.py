# 15990 :1,2,3 더하기 5
# https://kwangkyun-world.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-15990-%EB%B0%B1%EC%A4%80-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-5
# n=6일 때 , 
# dp[5]에서 2로 끝난거 +1 or 3으로 끝난거에 +1 ->dp[6][0]
# dp[4]에서 1로 끝난거에 +2 or 3으로 끝난거에 +2 ->dp[6][1]
# dp[3]에서 1로 끝난거에 +3 or 2로 끝난거에 +3 -> dp[6][2]
# 정리하면
# dp[i][0]=dp[i-1][1]+dp[i-1][2]
# dp[i][1]=dp[i-2][0]+dp[i-2][2]
# dp[i][2]=dp[i-3][0]+dp[i-3][1]


dp=[[0 for _ in range(3)] for i in range(100001)] # 다른 사이트 풀이도 찾아보기

dp[1]=[1,0,0] # 1로 끝나니까 [0]에 1할당 [1로 끝나는 경우의 수,2로 끝나는 경우의 수, 3으로 끝나는 경우의 수] => sum(dp[n])이 n에 해당하는 총 경우의 수
dp[2]=[0,1,0] # 2
dp[3]=[1,1,1] # 2+1,1+2,3로 각각 1,2,3으로 한번씩 끝나기에 [0]~[2]에 1씩 할당

for i in range(4,100001):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][0]+dp[i-2][2])%1000000009
    dp[i][2] = (dp[i-3][0]+dp[i-3][1])%1000000009

test_case=int(input())
for _ in range(test_case):
    n= int(input())
    print(sum(dp[n])%1000000009) # 나머지 정리에 의하여 for문에서도 나눠주고 마지막sum에서도 나눠줘야함