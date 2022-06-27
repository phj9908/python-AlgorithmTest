# 9613 : gcd합(최대공약수 누적합)

from itertools import combinations

def gcd(a,b): # 최대공약수 함수
    if b==0:
        return a
    return gcd(b,a%b)

for t in range(int(input())):
    arr=list(map(int,input().split()))
    sum=0
    
    for combination in list(combinations(arr[1:],2)):  
        if combination[0] > combination[1]:
            sum +=gcd(combination[0],combination[1])
        else:
            sum +=gcd(combination[1],combination[0])
    
    print(sum)
