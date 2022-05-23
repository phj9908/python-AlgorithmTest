# 2615 오목
import sys
sys.stdin=open('input.txt','r')
n=19
arr=[ list(map(int,sys.stdin.readline().strip().split())) for i in range(n)]
d=[(0,1),(1,0),(1,1),(1,-1)]

for i in range(n-5):
    for j in range(n-5):
        if arr[i][j]==0:
            continue
        if arr[i][j]==1:
            for dir in range(4):
                cnt = 0
                ny=i
                nx=j
                while range(5):
                    if arr[ny][nx]==1:
                        cnt+=1
                    if cnt==5:
                        if arr[i-d[dir][0]][j-d[dir][1]]!=1:
                            if ny+d[dir][0]<0 or ny+d[dir][0]>n-1 or nx+d[dir][1]<0 or nx+d[dir][1]>n-1 or arr[ny+d[dir][0]][nx+d[dir][1]]!=1:
                                print(1)
                                print(f'{i+1} {j+1}')
                                exit()
                        else:
                            break

                    ny +=d[dir][0]
                    nx +=d[dir][1]
                    if ny<0 or ny>n-1 or nx<0 or nx>n-1 or arr[ny][nx]!=1:
                        break

        if arr[i][j] == 2:
            for dir in range(4):
                cnt = 0
                ny = i
                nx = j
                while range(5):
                    if arr[ny][nx] == 2:
                        cnt += 1
                    if cnt == 5:
                        if arr[i - d[dir][0]][j - d[dir][1]] != 2:
                            if ny + d[dir][0] < 0 or ny + d[dir][0] > n - 1 or nx + d[dir][1] < 0 or nx + d[dir][
                                1] > n - 1 or arr[ny + d[dir][0]][nx + d[dir][1]] != 2:
                                print(2)
                                print(f'{i+1} {j+1}')
                                exit()
                        else:
                            break

                    ny += d[dir][0]
                    nx += d[dir][1]
                    if ny < 0 or ny > n - 1 or nx < 0 or nx > n - 1 or arr[ny][nx] != 2:
                        break
print(0)






