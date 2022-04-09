# 1961.숫자 배열회전




tc= int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[list(input().split()) for _ in range(n)]
    answer=[[0]*3 for i in range(n)]
    
    for i in range(n):
        ans=''
        for j in range(n-1,-1,-1):
            ans+=arr[j][i]
        answer[i][0]=ans
        
    for i in range(n-1,-1,-1):   
        ans=''
        for j in range(n-1,-1,-1):
            ans+=arr[i][j]
        answer[n-1-i][1]=ans
        
        ans=''
        for j in range(n):
            ans+=arr[j][i]
        answer[n-1-i][2]=ans
    
    print(f'#{t}')
    for i in answer:
        print(*i)
    
        
                   