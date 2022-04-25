def recur(idx,score,cal):
    if cal>l:
        return
    sum_score=max(sum_score,score)

    if idx>n:
        return
    recur(idx+1,score+arr[idx][0],score+arr[idx][1])
    recur(idx+1,score,cal)
    
n,l=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
sum_score=0
recur(0,0,0)
print(sum_score)
