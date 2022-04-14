#10570. 제곱 팰린드롬 수

# 수와 그 제곱수가 회문인지 확인하는 다른 방법(역순으로 읽기)
import math

def check(num):
    result=False
    sqrt_num=math.sqrt(num)
    num= str(num)

    if sqrt_num==float(int(sqrt_num)):
        sqrt_num=str(int(sqrt_num))

        if num==num[::-1] and sqrt_num == sqrt_num[::-1]:
            result=True
    return False


# 내 풀이
# import math
# tc=int(input())

# def check(arr):
#     arr=list(arr)
#     if len(arr)==1:
#         return True
#     for j in range(len(arr)//2):
#         if arr[j]!=arr[-1-j]:
#             return False
#     return True
                
# for t in range(1,tc+1):
#     a,b=map(int,input().split())
#     answer=0
#     for i in range(a,b+1):
#         n=str(i)
#         if check(n):
#             n=math.sqrt(i)
#             if int(n)**2==i:
#                 if check(str(int(n))):
#                     answer+=1

#     print(f'#{t} {answer}')
        

