#1934:최소공배수 구하기

n=int(input())
for i in range(n):
    ab = list(map(int,input().split()))
    ab_arr=ab.sort(reverse=True) # 내림차순
    A,B=ab[0],ab[1]
   
    while B!=0: # 최대공약수 먼저 구하기
        A=A%B
        A,B = B,A
    
    print(ab[0]*ab[1]//A)