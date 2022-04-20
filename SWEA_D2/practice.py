def dfs(arr, n, row):
    cnt=0

    if row==n:
        return 1

    for col in range(n):
        arr[row]=col

        for x in range(row):
            if arr[x]==arr[row]:
                break
            elif abs(arr[row]-arr[x])==row-x:
                break
        else:
            cnt+=dfs(arr,n,row+1)
    
    return cnt

n=int(input())
arr=[0]*n
print(dfs(arr,n,0))