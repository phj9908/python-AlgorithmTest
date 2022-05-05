#4615. 재미있는 오셀로 게임 ( 다시풀기 )
# 어디에 돌을 놓을지는 입력에서 정해짐, 돌을 놓기전 그때까지 만난 상대방돌들을 내돌색으로 바꿔주는 코드를 짜야함!
# 체크할때는 돌 하나에 대해서 !가장 가까운 같은 색의 돌!을 8 방향으로 찾는다!!
# 돌을 놓았을때 팔방을 검사해야 하며 상대방 돌인경우 좌표를 기억하고있다가 내돌을 만나는 경우 상대방 돌을 전부 자기 돌로 바꿔주는 작업이 가장 중요


# 상 하 좌 우 왼위 왼아 오위 오아
dx=[0,0,-1,1,-1,-1,1,1]
dy=[-1,1,0,0,-1,1,-1,1]

def stoneCheck(y,x,stone):
    if y<0 or y>n-1 or x<0 or x>n-1:    # 벽을 넘어가면
        return 0
    if arr[y][x]==0:    # 돌이 없으면
        return 0
    if arr[y][x]==stone:    # 같은색 돌이면
        return 2
    return 1    # 상대방 돌이라면

for t in range(1,int(input())+1):
    n,m=map(int,input().split())

    # 보드판 초기화
    arr=[[0]*n for i in range(n)]
    arr[n//2-1][n//2-1]=2
    arr[n//2][n//2-1]=1
    arr[n//2-1][n//2]=1
    arr[n//2][n//2]=2
    
    for _ in range(m):
        y,x,stone=map(int,input().split())
        y-=1    # 문제에서 (1,1)부터 시작하기에
        x-=1
        for j in range(8):  # 기준좌표(y,x)의 8방을 탐색하며 바꿔줘야하는 상대방 돌 탐색 및 색 변환
            d_x=0
            d_y=0            
            changeStone=[]  # 탐색할 동안 만난 상대방 돌들 저장소

            while 1:        # 8방향 중 한방향 계속 탐색
                d_x+=dx[j]
                d_y+=dy[j]                
                ny=y+d_y 
                nx=x+d_x

                res_stone=stoneCheck(ny,nx,stone)   # 돌이 없는지 이동이 가능한지 같은 색상을 만났는지 상대방 돌을 만났는지 판단
                if res_stone==0:
                    break                           # 돌이없거나 범위 아웃이면 그 방향 탐색 종료
                if res_stone==1:
                    changeStone.append((ny,nx))
                else:
                    for c_y,c_x in changeStone: # 지금까지 저장한 상대방 돌들의 색을 내돌색으로 바꾸기
                        arr[c_y][c_x]=stone
                    break

        arr[y][x]=stone # 8방 탐색후 기준좌표에 돌 놓기

    w_cnt=0
    b_cnt=0
    for i in arr:
        b_cnt+=i.count(1)
        w_cnt+=i.count(2)
    print(f'#{t} {b_cnt} {w_cnt}')



        
