#17087 숨바꼭질6 : 유클리드 호제법 활용
# 수빈이의 위치와 각 동생들이 위치한 지점까지의 거리들 사이 최대공약수 구하기
n,s = map(int,input().split())
a=list(map(int,input().split()))
res=0

def gcd(a,b):
    if b==0:
        return a
    else :
        return gcd(b,a%b)

dif=[]
for i in range(n): # 각 동생들과 수빈이 사이 거리 도출
    dif.append(abs(a[i]-s)) 
b=dif[0]
for i in range(1,n): # 첫번째 수와 두번째 수의 최대공약수 구한 뒤, 그 최대공약수와 세번째 수 의 최대공약수 구하고...마지막까지 반복
    b= gcd(b,dif[i])

print(b)
