# 13164 행복유치원
n,k=map(int,input().split())
arr=list(map(int,input().split()))
if n==1:
    print(0)
    exit()
if k==1:
    print(arr[-1]-arr[0])
    exit()
