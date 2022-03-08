# 9613 : gcd합(최대공약수 누적합)

from itertools import combinations


n=int(input())

def gcd(a,b): # 최대공약수 구하기
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for i in range(n):
    arr = list(map(int,input().split()))
    sum=0
    for j in range(1,len(arr)-1): # 맨앞의 수는 입력할 수의 갯수임!
        for k in range(j+1,len(arr)):
            sum +=gcd(arr[j],arr[k])
    print(sum)

# for j in range(1,len(arr)-1): # 맨앞의 수는 입력할 수의 갯수임
#         for k in range(j+1,len(arr)):
#             sum +=gcd(arr[j],arr[k])
#
# 위의 이중 for문 말고도 combinations(리스트,짝지을 구성원 수)으로도 가능
# ex) list=[1.2.3] , combinations(list,2) = [(1,2),(2,3)] , ( (1,2)와 (2,1)를 하나로 취급 )
#
# for j in list(combinations(arr[1:],2)):  
#     if j[0] > j[1]:
#         sum +=gcd(j[0],j[1])
#     else:
#         sum +=gcd(j[1],j[0])
