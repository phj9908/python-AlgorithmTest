# 2212 센서 (13164 행복유치원과 유사)
n=int(input())
k=int(input())
arr=list(map(int,input().split()))
arr.sort()
dif=[]
for i in range(len(arr)-1):
    dif.append(arr[i+1]-arr[i])
dif.sort()
print(sum(dif[:len(dif)-(k-1)]))
