# 2005 파스칼의 삼각형

tc= int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    arr[0][0]=1
    for i in range(1,n):
        for j in range(i+1):
            if j==0  or j==i:
                arr[i][j]=1
            else:
                arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    print(f'#{t}')
	
    for i in arr:
        for j in i:
            if j==0:
                continue
            else:
                print(j,end=' ')
        print()