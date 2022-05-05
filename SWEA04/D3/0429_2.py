# 11315. 오목 판정(다시)

# 우 하 왼아 오아(특정 방향을 검사했다면 반대편 방향은 검사하지 않아도 되기에 대각선 왼위 오위는 생략)
dir=[(0,1),(1,0),(1,-1),(1,1)]

def check(y,x):
    global answer

    if arr[y][x]=='o':
        for d in range(4):
            ny=y
            nx=x

            cnt=0
            while 0<=ny<n and 0<=nx<n and arr[ny][nx]=='o':
                cnt+=1
                ny+=dir[d][0]
                nx+=dir[d][1]
            if cnt>=5:
                answer='YES'
                return 1
    return 0

for t in range(1,int(input())+1):
    n=int(input())
    arr=[input() for i in range(n)]
    answer='NO'

    for y in range(n):
        for x in range(n):
            if check(y,x):
                break
        else:
            continue # break에 안걸린다면 계속
        break # break에 걸렸다면 모든 반복문 탈출

    print(f'#{t} {answer}')



        
