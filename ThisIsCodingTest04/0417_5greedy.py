# 큰수의 법칙
n,m,k = map(int,input().split())
arr=sorted(list(map(int,input().split())),reverse=True)
answer=0
k__=k
while m>0:
    if k__>0:
        answer+=arr[0]
        k__-=1
    else:
        answer+=arr[1]
        k__=k
    m-=1
print(answer)