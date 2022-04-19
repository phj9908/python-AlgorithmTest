# 게임 개발(다시 풀어보기)
n,m=map(int,input().split())
x,y,d_n=map(int,input().split())
arr=[ list(map(int,input().split())) for i in range(m)]

x=(n-1)-x # x는 서쪽으로 부터 떨어진 칸의 갯수라서
d=[(-1,0),(0,1),(1,0),(0,-1)]
visited=[[0]*n for i in range(m)]
visited[x][y]=1 # 현재 좌표 방문 처리

def turn_left(): # 왼쪽으로 회전
    global d_n
    d_n -=1
    if d_n== -1: # 인덱스 아웃 예외처리
        d_n=3

cnt=1 # 현재좌표방문한 거 미리 count
turn=0
while 1:
    turn_left()

    nx=x+d[d_n][1]
    ny=y+d[d_n][0]
    if visited[nx][ny]==0 and arr[nx][ny]==0: # 방문 안해본 육지라면
        visited[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn=0
        continue # 이건 굳이 왜하는 건가?

    else: # 회전했는데 가본 칸이나 바다일 때
        turn+=1
    
    if turn==4: # 4방향 모두 갈 수 없을 때
        nx=x-d[d_n][1] # back
        ny=y-d[d_n][0]

        if arr[nx][ny]==0: # back했는데 육지라면
            x=nx
            y=ny
        else: 
            break
        turn=0

print(cnt)

    