arr=[0]*20+[1]*20
for i in range(0,len(arr),20):
    print(*arr[i:i+20])

