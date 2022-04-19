# 1493. 수의 새로운 연산
tc=int(input())
arr= [[0]*301 for i in range(301)]
k=1
for i in range(1,301):
    arr[i][1]=k
    k+=1
    right=1
    while i>1:
        arr[i-1][1+right]=k
        k+=1
        right+=1
        i-=1

def fun(a,b):
    x=a[0]+b[0]
    y=a[1]+b[1]
    return arr[x][y]

def idx_return(num):
    p=num[0]
    q=num[1]
    num_idx=[]

    for i in range(301):
        for j in range(301):
            if arr[i][j]==p:
                num_idx.append((i,j))            
            if arr[i][j]==q:
                num_idx.append((i,j))
    return num_idx

for t in range(1,tc+1):
    num=list(map(int,input().split()))
    num_idx=idx_return(num)
    answer=fun(num_idx[0],num_idx[1]) 
    print(f'#{t} {answer}')