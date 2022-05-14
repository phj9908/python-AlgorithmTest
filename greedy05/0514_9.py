#11047 동전
n,k = map(int,input().split())
arr=[]
for i in range(n):
    a= int(input())
    if a<=k:
        arr.append(a)
answer=0
while k>0:
    x=arr.pop()
    if k>=x:
        answer+=k//x
        k%=x
print(answer)
