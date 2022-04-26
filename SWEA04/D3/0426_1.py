# 1860. 진기의 최고급 붕어빵
tc=int(input())
for test in range(1,tc+1):
    n,m,k=map(int,input().split())
    time=sorted(list(map(int,input().split())))
    t=0
    answer='Possible'
    bbang=0

    while t<=max(time):
        if time[0]==0:
            answer='Impossible'
            break

        t+=1
        if t%m==0:
            bbang+=k
        if t in time:
            if bbang:
                bbang-=1
                
            else:
                answer='Impossible'
                break

    print(f'#{test} {answer}')
            