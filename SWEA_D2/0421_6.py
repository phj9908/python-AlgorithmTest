# 1873. 상호의 배틀필드( 샘플은 맞췄는데 다른 테케 틀림.......)
tc=int(input())
for t in range(1,tc+1):
    h,w= map(int,input().split())
    arr=[ list(input()) for i in range(h)]
    n=int(input())
    str=list(input())

    #serch_list = ['<', '>', '^', 'v']
    y,x=0,0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    d=[0,0]

    for i in range(h):
        for j in range(w):
            if arr[i][j]=='<':
                y,x=i,j
                d=[dy[3],dx[3]]
                break
            elif arr[i][j]=='>':
                y,x=i,j
                d=[dy[1],dx[1]]
                break
            elif arr[i][j]=='v':
                y,x=i,j
                d=[dy[0],dx[0]]
                break
            elif arr[i][j]=='^':
                y,x=i,j
                d=[dy[2],dx[2]]
                break   
        else : continue # break에 안 걸렸다면
        
        break #  if문 안의 break에 걸렸다면 전체 반복문 나가기

    while str:
        com=str.pop(0)
        if com=='S':
            if x+d[1]<=w-1 and x+d[1]>=0 and y+d[0]>=0 and y+d[0]<=h-1 and arr[y+d[0]][x+d[1]]!='#':
                nx=x
                ny=y
                while 1:
                    ny+=d[0]
                    nx+=d[1]
                    if nx>w-1 or nx<0 or ny<0 or ny>h-1:
                        break
                    if arr[ny][nx]=='*':
                        arr[ny][nx]='.'
                        break
        if com=='U':
            d=[dy[2],dx[2]]
            arr[y][x]='^'
            if y+dy[2]>=0 and arr[y+dy[2]][x+dx[2]]=='.':
                arr[y][x]='.'
                arr[y+dy[2]][x+dx[2]]='^'
                y+=dy[2]
                x+=dx[2]
                
                
        if com=='D':
            d=[dy[0],dx[0]]
            arr[y][x]='v'
            if y+dy[0]<h and arr[y+dy[0]][x+dx[0]]=='.':
                arr[y][x]='.'
                arr[y+dy[0]][x+dx[0]]='v'
                y+=dy[0]
                x+=dx[0]
                

        if com=='L':
            d=[dy[3],dx[3]]
            arr[y][x]='<'
            if x+dx[3]>=0 and arr[y+dy[3]][x+dx[3]]=='.':
                arr[y][x]='.'
                arr[y+dy[3]][x+dx[3]]='<'
                y+=dy[3]
                x+=dx[3]
                

        if com=='R':
            d=[dy[1],dx[1]]
            arr[y][x]='>'
            if x+dx[1]<w and arr[y+dy[1]][x+dx[1]]=='.':
                arr[y][x]='.'
                arr[y+dy[1]][x+dx[1]]='>'
                y+=dy[1]
                x+=dx[1]
                

    print(f'#{t}',end=' ')
    for i in range(h):
        print(''.join(arr[i]))

    