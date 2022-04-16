# 6692. 다솔이의 월급 상자
tc= int(input())
for t in range(1,tc+1):
    n=int(input())
    answer=0
    for i in range(n):
        p, x=input().split()
        answer+=float(p)*int(x)
        
    print(f'#{t}',end=' ');print('{:.6f}'.format(answer)) # 소수점 6자리까지 출력