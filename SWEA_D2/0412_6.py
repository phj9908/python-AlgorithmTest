#1217. 거듭제곱

def fun(num,k):
    if k==1:
        return num
    return fun(num*n,k-1)

for t in range(1,11):
    tc=int(input())
    n,k =map(int,input().split())
    num=n
    n=fun(num,k)

    print(f'#{t} {n}')