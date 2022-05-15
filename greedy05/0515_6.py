# 2812 크게만들기
n,k =map(int,input().split())
num=list(input())
if num==sorted(num,reverse=True):
    num=num[:len(num)-k]
    print(int(''.join(num)))
    exit()
while k>0:
    for i in range(len(num)-1):
        if int(num[i])<int(num[i+1]):
            num[i]=''
            k-=1
            if k==0:
                break
    num=list(''.join(num))
print(int(''.join(num)))
