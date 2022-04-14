#1225. 암호생성기

for _ in range(1,11):
    t=int(input())
    num=list(map(int,input().split()))
    x=1
    while 1:
        n=num.pop(0)
        if n-x<=0:
            num.append(0)
            break    
        num.append(n-x)

        x+=1
        if x==6:
            x=1
    print(f'#{t}',end=' ');print(*num)