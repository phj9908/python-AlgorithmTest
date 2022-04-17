# 1이 될 때 까지 : (최소 연산횟수를 위한) 나누기 연산을 더 하도록
n,k=map(int,input().split())
answer=0
while n>1:
    if n%k==0:
        n//=k
    else:
        n-=1
    answer+=1
print(answer)
    