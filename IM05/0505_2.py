# 2563 색종이
n=int(input())
arr=[[0]*100 for i in range(100)]
for _ in range(n):
    x,y=map(int,input().split())
    x-=1
    y-=1
    for i in range(y,y+10):
        for j in range(x,x+10):
            if arr[i][j]==1:
                continue
            arr[i][j]=1
answer=0
for i in arr:
    answer+=i.count(1)
print(answer)
