# 1954 달팽이 숫자(다시 풀어보기)
#https://jennnn.tistory.com/3

tc=int(input())

#      우 하 좌 상 
d_row=[0,1,0,-1]
d_col=[1,0,-1,0]

for t in range(1,tc+1):
    num=int(input())
    arr=[ [0]*num for i in range(num) ]

    r,c=0,0 # 초기 위치
    dir=0 # 초기 방향 # 0:우, 1:하, 2:좌 , 3:상

    for n in range(1,num**2+1):
        arr[r][c]=n
        r+=d_row[dir] 
        c+=d_col[dir]

        # 범위벗어나거나 이미 값이 있을 땐 back했다가 방향 바꿔 go
        if r<0 or c<0 or r>=num or c>=num or arr[r][c]!=0:
            r-=d_row[dir]   # back 하고
            c-=d_col[dir]

            dir= (dir+1)%4 # 0,1,2,3을 벗어나지 않도록
            r+=d_row[dir]   # 다시 go
            c+=d_col[dir]

    print(f'#{t}')
    for i in arr:
        print(*i)


