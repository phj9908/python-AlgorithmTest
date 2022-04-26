def recur(subset,idx):
    global cnt

    if idx>=n:
        return
    subset.append(arr[idx])
    if sum(subset)==k:
        cnt+=1

    recur(subset,idx+1)
    subset.pop()
    recur(subset,idx+1)

n,k=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
recur([],0)




