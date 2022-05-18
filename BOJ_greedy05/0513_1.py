# 14916 거스름돈
n=int(input())
answer=0
while n>0:
    if n%5==0:
        answer+=n//5
        n%=5
    else:
        n-=2
        answer+=1
if n<0:
    print(-1)
else:
    print(answer)

