#6019. 기차 사이의 파리 
#두 기차가 서로 마주치느 시간= 두 기차사이 거리/두 기차의 속력의 합

tc=int(input())
for t in range(1,tc+1):
    d,a,b,f= map(int,input().split())
    x= d/(a+b)
    y= x*f
    print(f'#{t}',end=' ');print('{:.6f}'.format(y))

