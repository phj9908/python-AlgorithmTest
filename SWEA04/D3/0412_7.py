# 1289.원재의 메모리 복구
tc=int(input())

for t in range(1,tc+1):
    dst=list(input()) # ['0','0','1','1']
    src=list('0'*len(dst)) # ['0','0','0','0']
    cnt=0
    n=0
    while n!=len(dst):
        if dst[n]!=src[n]:
            src[n:]=dst[n]*(len(dst)-n)
            cnt+=1
        n+=1
    print(f'#{t} {cnt}')
            

