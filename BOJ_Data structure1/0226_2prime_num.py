#6588 : 골드바흐의 추측,소수 찾기 응용
# 수가 주어졌을 때, 그 수를 두 홀수 소수의 합 으로 나타내기.(2제외 모든 소수는 홀수)
import sys

# 시간초과 방지를 위해 소수리스트 먼저 생성하기
sieve_num =1000000+1 #인덱스 0부터 시작하기에 계산 편히 하기위해 +1
sieve=[True]*sieve_num
for i in range(2,int(sieve_num**0.5)+1):
    if sieve[i]:
        for j in range(2*i,sieve_num,i):
            sieve[j]=False

while 1:
    n= int(sys.stdin.readline())

    if n==0:
        break

    for i in range(3,n): # 홀수 소수 한정이기에 2제외
        if sieve[i] :
            if sieve[n-i]: 
                print('%d = %d + %d'%(n,i,n-i))
                break
    else:
        print("Goldbach's conjecture is wrong.")

    

                
