# 1491. 원재의 벽 꾸미기(완전 탐색)
tc=int(input())
for t in range(1,tc+1):
    n,a,b=map(int,input().split())
    answer=-1

    for i in range(1,n+1): # 이중 반복문으로 i,j 1씩 증가시키며 값찾기
        j=1
        while i*j<=n:
            ans=a*abs(i-j)+b*(n-i*j)
            if answer==-1:
                answer=ans
            else:
                answer=min(answer,ans)
            j+=1
    print(f'#{t} {answer}')
