# 국영수
n=int(input())
arr=[]
for i in range(n):
    str=list(input().split())
    arr.append(str)
arr=sorted(arr,key=lambda x:(int(-x[1]),int(x[2]),int(-x[3]),int(x[0])))
for i in arr:
    print(i[0])