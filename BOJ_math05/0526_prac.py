num=10000
sieve=[False]*2+[True]*(num-2)
for i in range(2,int(num**0.5)+1):
    for j in range(2*i,num,i):
        sieve[j]= False

a=int(input())
b=int(input())
sum=0
_min=b
for i in range(a,b+1):
    if sieve[i]:
        sum+=i
        _min=min(_min,i)


