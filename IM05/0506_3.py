#10163 색종이
n=int(input())
arr=[[0]*1001 for i in range(1001)]
answer=[]
for nn in range(1,n+1):
    x,y,w,h=map(int,input().split())
    for hh in range(y,y+h):
        arr[hh][x:x+w]=[nn]*w # >> 아래의 2중 포문 보다 시간 절약
    # for hh in range(h):
    #     for ww in range(w):
    #         arr[y+hh][x+ww]=nn
for nn in range(1,n+1):
    sum=0
    for i in arr:
        sum+=i.count(nn)
    print(sum)

