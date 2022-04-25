# 11387. 몬스터 사냥
tc=int(input())
for t in range(1,tc+1):
    d,l,n=map(int,input().split())
    answer=0
    for i in range(n-1):
        answer+=d*(1+n*l*0.01) 
    
    print(f'#{t} {int(answer)}')