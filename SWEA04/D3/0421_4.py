# 10580. 전봇대
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[]
    for i in range(n):
        a,b=map(int,input().split())
        arr.append((a,b))
    answer=0

    for left,right in arr:
        for i in arr:
            if (left<i[0] and right>i[1]) or (left>i[0] and right<i[1]):
                answer+=1
            
    print(f'#{t} {answer//2}') # A전선이 B전선을 지나는 경우와 B전선이 A전선을 지나는 경우 중복되기에 //2