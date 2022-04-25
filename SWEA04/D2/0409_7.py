# 1959. 두개의 숫자열

# 다른풀이
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


# 내 코드 (너무 복잡하게 풀었다..)
tc=int(input())
for t in range(1,tc+1):
    n,m=map(int,input().split())
    dif=abs(n-m)
    if n<m:
        a=[0]*dif+list(map(int,input().split()))
        b=list(map(int,input().split()))
    elif n>m:
        a=list(map(int,input().split()))
        b=[0]*dif+list(map(int,input().split()))
    sum=0
    arr=[]

    if n<m:
        arr.append(a.copy())
        while dif>0:
            a.append(a.pop(0))
            arr.append(a.copy())
            dif-=1
        
        for i in range(len(arr)):
            s=0
            for j in range(len(a)):
                s+=arr[i][j]*b[j]
            sum=max(sum,s)
    
    elif n>m:
        arr.append(b.copy())
        while dif>0:
            b.append(b.pop(0))
            arr.append(b.copy())
            dif-=1
        
        for i in range(len(arr)):
            s=0
            for j in range(len(b)):
                s+=arr[i][j]*a[j]
            sum=max(sum,s)
    
    else:
        for i in range(len(a)):
            sum=a[i]*b[i]

    print(f'#{t} {sum}')

            
  
    
    