d=[(0,1),(1,0),(1,1),(-1,1)]

def check(y,x):
    global answer

    if arr[y][x]=='o':
        for i in range(4):

            ny=y
            nx=x
            cnt=0
            while 0<=ny<n and 0<=nx<n and arr[ny][nx]=='o':
                cnt+=1
                ny+=d[i][0]
                nx+=d[i][1]
            if cnt>=5:
                answer='YES'
                return 1
    return 0





for t in range(1,int(input())+1):
    n=int(input())
    arr=[input() for _ in range(n)]
    answer='NO'

    for i in range(n):
        for j in range(n):
            if check(i,j):
                break
        else:
            continue
        break

    print(f'#{t} {answer}')