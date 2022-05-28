#10570. 제곱 팰린드롬 수

# 수와 그 제곱수가 회문인지 확인하는 다른 방법: 정방향으로 읽은 문자열 == 역방향으로 읽은 문자열 일치여부확인)
import math

def check(num):
    result=False
    sqrt_num=math.sqrt(num)
    num= str(num)

    if sqrt_num.is_integer(): # 루트씌운 수가 정수가 아닌수를 거르기
        sqrt_num=str(int(sqrt_num))

        if num==num[::-1] and sqrt_num == sqrt_num[::-1]:
            result=True
    return False


# 내 풀이
# import math
# tc=int(in.txt())

# def check(arr):
#     arr=list(arr)
#     if len(arr)==1:
#         return True
#     for j in range(len(arr)//2):
#         if arr[j]!=arr[-1-j]:
#             return False
#     return True
                
# for t in range(1,tc+1):
#     a,b=map(int,in.txt().split())
#     answer=0
#     for i in range(a,b+1):
#         n=str(i)
#         if check(n):
#             n=math.sqrt(i)
#             if int(n)**2==i: # 루트씌운 수가 정수가 아닌수를 거르기 
#                 if check(str(int(n))):
#                     answer+=1

#     print(f'#{t} {answer}')
        

