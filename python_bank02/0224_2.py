# 수정 필요
n,m=map(int,input().split())
arr =[] 

for i in range(n):# 한번에 2차원배열 입력받기
    arr.append(list(map(int,input().split()))) 

x=m-1
y=n-1
day=0

while arr and arr.count(1)!=m*n :
    if arr[x-1][y] == 0 and arr[x][y-1] ==0:
        arr[x][y-1]=1
        x -=1;arr[x][y]=1
        day+=1
    elif arr[x-1][y] ==0:
        x-=1 
        arr[x][y]=1
        day+=1
    elif arr[x][y-1] ==0:
        y-=1
        arr[x][y]=1
        day+=1
print(day)