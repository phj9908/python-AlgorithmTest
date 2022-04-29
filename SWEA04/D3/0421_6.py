# 1873. 상호의 배틀필드( 다시풀기.. )

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
command_dict = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' :4,
                '^' : 0, 'v' : 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2:'<', 3:'>'} # 상하좌우 순대로 value값이 0,1,2,3 (move_list의 인덱스와 일치)
serch_list = ['<', '>', '^', 'v']

tc=int(input())
for t in range(1,tc+1):
    h,w= map(int,input().split())
    arr=[ list(input()) for i in range(h)]
    n=int(input())
    commands=input()

    for i in range(h):
        for j in range(w):
            if arr[i][j] in serch_list:
                tank_pos=(i,j,command_dict[arr[i][j]])
                break
        else: 
            continue # break에 안걸리면 계속 진행
        break    # break에 걸렸다면 모든 반복문 탈출

    for com in commands:
        temp=command_dict[com]

        if temp==4: # 포탄 발사라면
            dy=tank_pos[0] # 탱크가 바라보는 방향(위치)
            dx=tank_pos[1]

            while 1:
                dy+=move_list[tank_pos[2]][0]
                dx+=move_list[tank_pos[2][1]]

                if dy<0 or dy>h-1 or dx<0 or dx>w-1 or arr[dy][dx]=='#':
                    break
                if arr[dy][dx]=='*':
                    arr[dy][dx]='.'
                    break
        else: # 이동 명령이라면
            y=tank_pos[0]
            x=tank_pos[1]
            dy=y+move_list[temp][0]
            dx=x+move_list[temp][1]

            tank_pos=(y,x,temp)
            if h>dy>=0 and w>dx>=h and arr[dy][dx]=='.':
                arr[y][x]='.' # 기존 위치를 평지로 바꾸기
                arr[dy][dx]=command_dict[temp]  # 가야하는 위치에 탱크표시
                tank_pos=(dy,dx,temp) # 탱크위치 갱신

    print(f'#{t}',end=' ')
    for i in arr:
        print(''.join(i))

    