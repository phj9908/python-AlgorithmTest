# 2745 진법 변환
arr='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=input().split()
b=int(b)

sum=0
for i in range(len(n)-1,-1,-1):
    sum+=(b**(len(n)-1-i))*arr.index(n[i])
print(sum)
