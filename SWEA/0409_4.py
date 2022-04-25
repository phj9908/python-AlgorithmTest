# 쉬운 거스름돈

list=[50000,10000,5000,1000,500,100,50,10]
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[]
    while n>10:
        for i in list:
            arr.append(n//i)
            n%=i
    print(f'#{t}');print(*arr)