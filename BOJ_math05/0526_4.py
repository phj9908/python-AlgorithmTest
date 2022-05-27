# 9613 gcd합( 여러 수들의 최대공약수 누적합, 다시보기)

from itertools import combinations

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

for _ in range(int(input())):
    arr=list(map(int,input().split()))
    total=0

    for com in list(combinations(arr[1:],2)): # 여러수들을 2개씩 조합
        if com[0]> com[1]: # 더 큰수가 뒤에 감
            total+=gcd(com[1],com[0])
        else:
            total+=gcd(com[0],com[1])

    print(total)