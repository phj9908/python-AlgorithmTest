# 게임 개발(다시 풀어보기)
n,m=map(int,input().split())
y,x,d_n=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
d=[[0,-1],[1,0],[0,1],[-1,0]]
x=(m-1)-x   # x는 서쪽으로 부터 떨어진 칸의 갯수
visited=[[0]*m for i in range(n)]
visited[y][x]=1 # 현재 좌표 방문 처리
cnt=1   # 현재좌표방문한 거 미리 count
turn=0

while 1:
    d_n-=1  # 왼쪽으로 90도씩 회전
    if d_n==-1: # 인덱스 아웃 예외처리
        d_n=3
    
    ny=y+d[d_n][0] 
    nx=x+d[d_n][1]
    # 그냥 y-=d[d_n][0] 이런식으로 하면 오답나옴!

    if visited[ny][nx]==0 and arr[ny][nx]==0:    # 방문 안해본 육지라면
        visited[ny][nx]=1
        cnt+=1
        turn=0
        continue # 아래의  조건문들 pass

    else:   # 회전했는데 가본 칸이나 바다일 때
        turn+=1

    if turn==4: # 4방향 모두 갈 수 없을 때
        ny=y-d[d_n][0]
        nx=x-d[d_n][1]
        if arr[ny][nx]==0:  # back했는데 육지라면
            y=ny
            x=nx
        else:
            break
        turn=0

print(cnt)
            
    