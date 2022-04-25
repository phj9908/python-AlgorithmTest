# 시각 덧셈

tc=int(input())
for t in range(1,tc+1):
    h1,m1,h2,m2=map(int,input().split())
    
    m=(m1+m2)%60
    h=(h1+h2)%12+(m1+m2)//60
    
    print(f'#{t} {h} {m}')