# 3131. 100만 이하의 모든 소수
n=1000000
sieve=[True]*n
for i in range(2,int(n**0.5)+1):
    for j in range(2*i,n,i):
        sieve[j]=False

for i in range(2,len(sieve)):
    if sieve[i]:
        print(i,end=' ')