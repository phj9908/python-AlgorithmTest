# 3376. 파도반 수열
tc=int(input())
arr=[0,1,1,1]
for t in range(1,tc+1):
    n=int(input())
    arr+=[0]*(n-4+1)
    for i in range(1,n+1-3):
        arr[i+3]=arr[i]+arr[i+1]

    print(f'#{t} {arr[n]}')
    
    
        