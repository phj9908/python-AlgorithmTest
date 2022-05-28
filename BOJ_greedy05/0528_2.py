#Byte Coin(단순하게 풀기, 다시풀기)
n,w=map(int,input().split())
arr=[ int(input()) for i in range(n)]
coin=0
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]: # 다음날 상승한다면 매수
        if w//arr[i]>0:
            coin=w//arr[i]
            w%=arr[i]
    elif arr[i]>arr[i-1]: # 다음날 하강한다면 매도
        w+=coin*arr[i]
        coin=0

if coin>0:
    w+=coin*arr[-1]
print(w)



