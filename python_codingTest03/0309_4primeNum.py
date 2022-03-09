# 에라스토테네스의 체
# 연속된 소수끼리의 합으로 n이 되는지 확인하는 함수

sieve=[]

def prime(n):
    global sieve # 리턴값이 따로 없기에 이거 해줘야 됨!!! 아님 answer()에선 sieve=[]로 전달받음
    n=n+1
    sieve=[True]*n
    for i in range(2,int(n**0.5)+1):
        for j in range(2*i,n,i):
            sieve[j]=False
            
def answer(n):
    
    prime(n)    # n까지 소수 체크
    prime_nums=[]
    for i in range(2,n+1):
        if sieve[i]:
            prime_nums.append(i)
            if sum(prime_nums)==n:
                print(f'연속된 소수 {prime_nums}의 합은 {n}입니다.')
                break
    else:
        print(f'연속된 소수의 합으로 {n}을 만들 수 없습니다.')

answer(41)
answer(20)
                
