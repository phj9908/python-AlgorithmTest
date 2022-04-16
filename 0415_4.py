# 1208. [S/W 문제해결 기본] 1일차 - Flatten
for t in range(1,11):
    dump=int(input())
    arr=list(map(int,input().split()))

    while dump>0:
        arr.sort()

        arr[-1]-=1
        arr[0]+=1

        dump-=1
    
    arr.sort()
    print(f'#{t} {arr[-1]-arr[0]}')

        
