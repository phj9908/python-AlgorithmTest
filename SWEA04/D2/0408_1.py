# 2001. 파리퇴치
tc=int(input())

for t in range(1,tc+1):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    answer=0
    for i in range(n-m+1): # m=2이면 n-1,m=3이면 n-2...
        for j in range(n-m+1):
            sum=0
            for y in range(m):
                for x in range(m):
                    sum+=arr[i+y][j+x]
            answer=max(answer,sum)
                
    print(f'#{t}',end=' ');print(answer)