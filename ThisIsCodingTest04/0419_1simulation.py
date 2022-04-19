# 상하좌우
n=int(input())
command= list(input().split())

#  하 좌 상 우
dx=[0,-1,0,1]
dy=[1,0,-1,0]

x,y=1,1

for i in command:
    if i=='U':
        if y+dy[2]>=1:
            x+=dx[2]
            y+=dy[2]
    elif i=='D':
        if y+dy[0]<=n:
            x+=dx[0]
            y+=dy[0]
    elif i=='R':
        if x+dx[3]<=n:
            x+=dx[3]
            y+=dy[3]
    else:
        if x+dx[1]>=1:
            x+=dx[1]
            y+=dy[1]
print(f'{y} {x}')
    
    


