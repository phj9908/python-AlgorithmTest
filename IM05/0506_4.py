# 13300 방배정
import math

n,k=map(int,input().split())
arr=[ [0]*2 for i in range(7)]
for i in range(n):
    s,y=map(int,input().split())
    arr[y][s]+=1
cnt=12
for i in arr[1:]:
    for j in i:
        if j>k:
            cnt+=math.ceil(j/k)-1
        if j==0:
            cnt-=1
print(cnt)

