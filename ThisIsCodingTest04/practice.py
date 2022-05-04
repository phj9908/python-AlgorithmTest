n,m=map(int,input().split())
y,x,d_n=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

d=[(0,-1),(1,0),(0,1),(-1,0)]
visited=[[0]*m for i in range(n)]
visited[y][x]=1
turn=0
cnt=0
x=(m-1)-x

while 1:
    d_n-=1
    if d_n==-1:
        d_n=3
    ny=y+d[d_n][0]
    nx=x+d[d_n][1]

    if visited[ny][nx]==0 and arr[ny][nx]==0:
        visited[ny][nx]=1
        cnt+=1
        turn=0
        continue
    else:
        turn+=1
    if turn==4:
        ny=y-d[d_n][0]
        nx=x-d[d_n][1]
        if arr[ny][nx]==0:
            y=ny
            x=nx
        else:
            break
        turn=0

