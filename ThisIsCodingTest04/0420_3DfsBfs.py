# 미로탈출(다시풀기)
# dfs가 아닌! bfs
from collections import deque

n,m= map(int,input().split())
arr=[list(map(int,input())) for i in range(n)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    while queue:
        y,x=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if  0<ny<n-1 and 0<nx<m-1 and arr[ny][nx]==1:
                arr[ny][nx]=arr[y][x]+1 # 바로 전좌표의 가중치에 +1 해서 이때까지 이동한 거리 기록
                queue.append((ny,nx))

    return arr[n-1][m-1]

print(bfs(0,0))