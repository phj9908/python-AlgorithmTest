#1244 스위치 켜고 끄기
def change(x):
    if arr[x]:
        arr[x] = 0
    else:
        arr[x] = 1

n=int(input())
arr=[0]+list(map(int,input().split()))
people=int(input())
for _ in range(people):
    s,num=map(int,input().split())
    if s==1:
        for i in range(num,n+1,num):
            change(i)
    else:
        idx=1
        change(num)

        while 1<=num-idx and num+idx<=n:
            if arr[num-idx]==arr[num+idx]:
                change(num-idx)
                change(num+idx)
            else:
                break
            idx+=1
del arr[0]
for i in range(0,n,20):
    print(*arr[i:i+20])
