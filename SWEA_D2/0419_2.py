tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[[0]*n for i in range(n)]
    answer=0

    x,y=0,0
    while 1:
        arr[x][y]=1 
        #을 포함한 행열 대각선도 1로 