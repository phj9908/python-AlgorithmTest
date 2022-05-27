# 2745 진법 변환
arr='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=input().split()
b=int(b)

sum=0
n=n[::-1]
for i in range(len(n)):
    sum+=(b**i*arr.index(n[i]))
print(sum)
