#17103 골드바흐 파티션
# 2보다 큰 짝수는 두 소수의 합
import sys

sieve_num = 1000000+1
sieve=[False,False]+[True]*(sieve_num-2) # [0],[1]은 소수가 아니기에 미리 false

for i in range(2,int(sieve_num**0.5)+1):
    if sieve[i]:
        for j in range(2*i,sieve_num,i):
            sieve[j]=False

test_num=int(sys.stdin.readline())
for _ in range(test_num):
    n=int(sys.stdin.readline()) # 10일 때
    cnt=0

    for i in range(2,n):    
        if i>n-i: # (3,7)과 (7,3)의 경우, 중복 되기에 (i//2)+1해서 (5,5)까지만 for문
            break
         
        if sieve[i] and sieve[n-i]: 
            cnt+=1
    
    print(cnt)