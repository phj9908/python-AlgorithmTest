# 우 하 왼아 오아
dir=[(0,1),(1,0),(1,-1),(1,1)]

def check():
    global answer

    for y in range(n):
        for x in range(n):
            if arr[y][x]=='o':
                for d in range(4):
                    cnt=0
                    ny=y
                    nx=x
                    while 0<=ny<n and 0<=nx<n and arr[ny][nx]=='o':
                        ny+=dir[d][0]
                        nx+=dir[d][1]
                        cnt+=1
                    if cnt==5:
                        answer='YES'
                        return answer
    return 


for t in range(1,int(input())+1):
    n=int(input())
    arr=[ input() for i in range(n)]
    answer='NO'

    check()
    print(f'#{t} {answer}')