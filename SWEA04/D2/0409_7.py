# 1959. 두개의 숫자열

n,m= map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
answer=0

if n<m:
    for i in range(m-n+1): # 길이 차 +1 만큼 반복
        sum=0
        for j in range(n):  # 더 짧은 리스트의 크기만큼 곱셈 반복
            sum=a[j]*b[j+i]
        answer=max(answer,sum)
elif n>m:
    for i in range(n-m+1):
        sum=0
        for j in range(m):
            sum=b[j]*a[j+i]
        answer=max(answer,sum)
else:
    for i in range(len(a)):
        sum=a[i]*b[i]



            
  
    
    