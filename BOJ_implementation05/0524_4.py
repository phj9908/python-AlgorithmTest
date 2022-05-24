#16926 배열돌리기1
from collections import deque
import sys
sys.stdin=open('input.txt','r')

#n,m,r=list(map(int,input().split()))
n,m,r=4,4,2
arr=[ list(map(int,sys.stdin.readline().strip().split())) for i in range(n) ]
d=[(0,1),(1,0),(0,-1),(-1,0)]
min_k=min(n,m)//2
res_arr=deque([deque() for i in range(min_k)])

k=0
visited=[ [False]*m for i in range(n)]
while k<min_k:
    y,x=k,k
    dir=0
    while 1:
        visited[y][x]=True
        res_arr[k].append(arr[y][x])
        y+=d[dir][0]
        x+=d[dir][1]
        if y == k and x == k:  # 다시 시작점에 되돌아오면(직진하다가 시작점에 도달한 경우)
            k += 1
            break

        if y<0 or y>n-1 or x<0 or x>m-1 or visited[y][x]:
            y -= d[dir][0]
            x -= d[dir][1]
            dir=(dir+1)%4
            y += d[dir][0]
            x += d[dir][1]
            if y==k and x==k: # 다시 시작점에 되돌아오면(방향바꿨는데 시작점인 경우)
                k += 1
                break

for i in range(k):
    res_arr.rotate()

k=0
visited=[ [False]*m for i in range(n)]
while k<min_k:
    y,x=k,k
    dir=0
    while 1:
        visited[y][x]=True
        arr[y][x]=res_arr[k].popleft()
        y+=d[dir][0]
        x+=d[dir][1]

        if y<0 or y>n-1 or x<0 or x>m-1 or visited[y][x]:
            if y==k and x==k: # 다시 시작점에 되돌아오면
                break
            y -= d[dir][0]
            x -= d[dir][1]
            dir=(dir+1)%4
            y += d[dir][0]
            x += d[dir][1]
    k+=1

for i in arr:
    print(*i)



