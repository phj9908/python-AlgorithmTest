n=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)-1,0,-1):
    if arr[i-1]<arr[i]:
        swap=i-1
        break
else:
    print(-1)
    exit()

for i in range(len(arr)-1,0,-1):
    if arr[i]>arr[swap]:
        arr[i],arr[swap]=arr[swap],arr[i]
        arr=arr[:swap+1]+sorted(arr[swap+1:])
        print(*arr)
        break