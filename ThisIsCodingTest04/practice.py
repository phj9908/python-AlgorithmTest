# nx ny가 꼭 필요한가 그냥x,y하니까 오답임
n,m=map(int,input().split())
x,y,d_n=map(int,input().split())
arr=[ list(map(int,input().split())) for i in range(n) ]

x=(m-1)-x
d=[(-1,0),(0,1),(1,0),(0,-1)]
visited=[ [0]*m for i in range(n)]
visited[y][x]=1 

cnt=1
turn=0
while 1:
    d_n-=1
    if d_n==-1:
        d_n=3

    y+=d[d_n][0]
    x+=d[d_n][1]

    if visited[y][x]==0 and arr[y][x]==0:
        visited[y][x]=1
        cnt+=1
        turn=0
        continue
    else:
        turn+=1
    if turn==4:
        x-=d[d_n][1]
        y-=d[d_n][0]
        if arr[y][x]!=0:
            break
        turn=0
print(cnt)
