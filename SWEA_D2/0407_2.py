# 1926 369 게임

n=int(input())
list=['3','6','9']
for i in range(1,n+1):
    s=str(i)
    if '3' in s or '6' in s or '9' in s: 
        cnt=0
        for j in s:
            if j in list:
                cnt+=1
        if cnt==len(s):
            print('-'*cnt,end=' ')
        else:print('-',end=' ')
    else:
        print(i,end=' ')