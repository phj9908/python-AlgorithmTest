#10157 자리배정
import sys
input = sys.stdin.readline

c,r=map(int,input().split())
k=int(input())
y,x=1,1
arr=[[0]*(c+1) for i in range(r+1)]
d=[(1,0),(0,1),(-1,0),(0,-1)] # 상 우 하 좌
dir=0

if k>c*r:
    print(0)
    exit()

for n in range(1,c*r+1):
    if n==k:
        print(f'{x} {y}')
        break

    arr[y][x] = n
    y+=d[dir][0]
    x+=d[dir][1]
    if x<1 or x>c or y<1 or y>r or arr[y][x]!=0:
        y-=d[dir][0]
        x-=d[dir][1]
        dir= (dir+1)%4

        y+=d[dir][0]
        x+=d[dir][1]
