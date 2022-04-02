#1929 : 소수구하기

a,b = map(int,input().split())
sieve=[True]*(b+1)  # 인덱스가 0부터 시작하니까 실제 a~b범위에 맞추기 위해 b+1개 만들기

for i in range(2,int((b+1)**0.5)+1) :
    if sieve[i]:
        for j in range(2*i,b+1,i): # 범위내의 i의 배수들 제거
            sieve[j]=False
for i in range(a,b+1):
    if sieve[i]:
        print(i)
