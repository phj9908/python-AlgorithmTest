# 10200. 구독자 전쟁
tc= int(input())
for t in range(1,tc+1):
    n,a,b=map(int,input().split())
    
    if a+b>n:
        print(f'#{t} {min(a,b)} {a+b-n}')
    else:
        print(f'#{t} {min(a,b)} 0')
