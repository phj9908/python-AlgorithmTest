# 17276 배열돌리기( 구현문제 더 풀어보고,,다시풀기 )
#  https://eboong.tistory.com/302

def plus_turn(arr,n):
    mid=n//2
    for i in range(n):
        arr[i][i],arr[i][mid] = arr[i][mid],arr[i][i]
        arr[i][i],arr[i][n-1-i]=arr[n-1-i],arr[i]
        arr[mid][i],arr[i][i]=arr[i][i],arr[mid][i]

    for i in range(n):
        arr[mid][i].arr[mid][n-1-i]=arr[mid][n-1-i],arr[mid][i]

    return arr

def minus_turn(arr, n):
    mid = n // 2
    for i in range(n):
        arr[i][n-1-i], arr[i][mid] = arr[i][mid], arr[i][i]
        arr[i][i], arr[i][n - 1 - i] = arr[n - 1 - i], arr[i]
        arr[mid][i], arr[i][n-1-i] = arr[i][i], arr[mid][i]

    for i in range(n):
        arr[n-1-i][i].arr[i][n - 1 - i] = arr[i][n - 1 - i], arr[n-1-i][i]

    return arr

for _ in range(int(input())):
    n,d=map(int,input().split())
    arr=[ list(map(int,input().split())) for i in range(n)]
    if d>0:
        d//=45
        for _ in range(d):
            arr=plus_turn(arr,n)
        for i in arr:
            print(*i)
    else:
        d//=-45
        for _ in range(d):
            arr=minus_turn(arr,n)
        for i in arr:
            print(*i)







