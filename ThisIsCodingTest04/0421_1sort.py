# 두 배열의 원소 교체
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())),reverse=True)

for i in range(3):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]

print(sum(a))
