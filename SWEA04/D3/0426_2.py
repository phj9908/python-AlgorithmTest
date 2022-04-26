# 4698. 테네스의 특별한 소수
num=1000001
sieve=[False,False]+[True]*(num-2)
for i in range(2,int(num**0.5)+1):
    for j in range(2*i,num,i):
        sieve[j]=False

tc=int(input())
for t in range(1,tc+1):
    d,a,b=map(int,input().split())
    cnt=0

    for i in range(a,b+1):
        if sieve[i]:
            if str(d) in str(i):
                cnt+=1
    print(f'#{t} {cnt}')
