# 5618 공약수(이중포문은 시간초과, 다시출기)
# 두 수의 공약수는 두 수의 최대공약수의 약수이다.!! https://pacific-ocean.tistory.com/177

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

n=int(input())
arr=list(map(int,input().split()))
gcd_num=gcd(arr[0],gcd(arr[1],arr[-1])) # n=2 or 3 이기에

for i in range(1,gcd_num//2+1):
    if gcd_num%i==0:
        print(i)
print(gcd_num)