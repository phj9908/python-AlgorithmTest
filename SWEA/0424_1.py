# 6485. 삼성시의 버스 노선(다시풀어보기)
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[]
    for i in range(n):
        a,b=map(int,input().split())
        arr.append((a,b))
    p=int(input())
    p_hash={}
    for i in range(1,5001): # 5000개의 정류장중에 몇번까지 나올지 모르기때문에
        p_hash[i]=0
    
    for i in range(len(arr)):
        for j in range(arr[i][0],arr[i][1]+1):
            p_hash[j]+=1
    answer=[]
    for i in range(p):
        answer.append(p_hash[int(input())])

    print(f'#{t}',end=' ');print(*answer)