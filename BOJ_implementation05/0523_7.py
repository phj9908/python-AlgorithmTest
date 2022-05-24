# 2615 오목 (어디가 틀린건지 모르겠음)
import sys
sys.stdin=open('input.txt','r')
n=19
arr=[ list(map(int,sys.stdin.readline().strip().split())) for i in range(n)]
d=[(0,1),(1,0),(1,1),(1,-1)]

for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            for dir in range(4):
                cnt = 1
                ny=i+d[dir][0]
                nx=j+d[dir][1]
                while 1:
                    if ny < 0 or ny > n - 1 or nx < 0 or nx > n - 1 or arr[ny][nx] != arr[i][j]:
                        break
                    cnt += 1
                    if cnt==5:
                        if 0<=i-d[dir][0]<n and 0<=j-d[dir][1]<n and arr[i-d[dir][0]][j-d[dir][1]]==arr[i][j]:
                            break
                        if 0<=ny+d[dir][0]<n and 0<=nx+d[dir][1]<n and arr[ny+d[dir][0]][nx+d[dir][1]]==arr[i][j]:
                            break

                        if arr[i][j]==1:
                            print(1)
                        else:
                            print(2)
                        print(f'{i+1} {j+1}')
                        exit()

                    ny +=d[dir][0]
                    nx +=d[dir][1]
print(0)
