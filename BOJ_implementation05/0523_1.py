# 1913 달팽이
n=int(input())
p=int(input())
d=[(1,0),(0,1),(-1,0),(0,-1)] # 하우상좌
arr=[ [0]*n for i in range(n)]
x,y=0,0 # 시작
dir=0
p_y,p_x=-1,-1

for i in range(n**2,0,-1):
    if i==p:
        p_y,p_x=y,x

    arr[y][x]=i
    y+=d[dir][0]
    x+=d[dir][1]
    if 0>y or y>n-1 or 0>x or x>n-1 or arr[y][x]!=0:
        y-=d[dir][0]
        x-=d[dir][1]

        dir=(dir+1)%4

        y+=d[dir][0]
        x+=d[dir][1]
for i in arr:
    print(*i)
print(p_y+1,p_x+1)




