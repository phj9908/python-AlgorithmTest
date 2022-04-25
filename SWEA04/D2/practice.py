

n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append([0]+map(int,input.split())+[0])

answer=0
for i in range(n+1):
    
    cnt=0
    for j in range(n+1):
        if arr[i][j]=='0':
            if arr[i][j]!=arr[i][j+1]:
                cnt+=1
        else:
            if arr[i][j]==arr[i][j]:
                cnt+=1
            else:
                if cnt==k:
                    answer+=cnt
    cnt=0
    for j in range(n+1):
        if arr[j][i]==0:
            if arr[j][i]!=arr[j][i]:
                cnt+=1
        else:
            if arr[j][i]==arr[j][i]:
                cnt+=1
            else:
                if cnt==k:
                    answer+=cnt        
print(answer)
