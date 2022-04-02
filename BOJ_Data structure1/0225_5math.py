#1978 : 작은범위에서 소수찾기
n=int(input())
arr=list(map(int,input().split()))
cnt=0

for i in arr:
    err=0
    if i==1:
        continue
    else :
        for j in range(2,i): # N은 100이하 자연수
            if i%j==0:
                err+=1
                break
        if err==0:
            cnt+=1
print(cnt)

