# 2564 경비원(모서리에만 좌표가 있다는 조건>> 사각형을 일직선으로 펼치기!!)
# 다시풀어보자..
m,n=map(int,input().split())
store_n=int(input())
arr=[]
for i in range(store_n+1):
    d1,d2= map(int,input().split())
    if d1==1: # 북
        arr.append(2*n+m+d2)
    if d1==2: # 남
        arr.append(n+(m-d2))
    if d1==3: # 서
        arr.append(m+n+(n-d2))
    if d1==4: # 동(시작점)
        arr.append(d2)
answer=0
for i in range(store_n):
    ans=abs(arr[-1]-arr[i])
    answer+=min(ans,2*(m+n)-ans)
print(answer)






