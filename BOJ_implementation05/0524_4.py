#16926 배열돌리기1
from collections import deque
import sys
# sys.stdin=open('in.txt.txt','r')

n,m,r=list(map(int,input().split()))
arr=[ list(map(int,sys.stdin.readline().strip().split())) for i in range(n) ]
d=[(1,0),(0,1),(-1,0),(0,-1)] # 반시계방향
min_k=min(n,m)//2 # 겉의 사각형부터 맨 안쪽의 사각형까지 몇번 들어가야 하는지(문제 조건 참고)
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

for _ in range(r):
    for i in range(k):
        res_arr[i].rotate()

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
            if y==k and x==k: # 다시 시작점에 되돌아오면(방향바꿨는데 시작점인 경우)
                k += 1
                break
    k+=1

for i in arr:
    print(*i)



