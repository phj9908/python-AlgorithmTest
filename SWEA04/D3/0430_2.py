# 3304. 최장 공통 부분 수열 (다시 풀기)
# https://deok2kim.tistory.com/143 

for t in range(1,int(input())+1):
    #words=list(in.txt())
    a,b=input().split()
    a=' '+a
    b=' '+b
    
    dp=[ [0]*len(a) for _ in range(len(b))]

    for i in range(1,len(b)):
        for j in range(1,len(a)):
            if b[i]==a[j]:          # 같을 때
                dp[i][j]=dp[i-1][j-1]+1
            else:                   # 다를 때
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    answer=dp[-1][-1] 
    print(f'#{t} {answer}')
