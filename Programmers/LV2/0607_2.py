# 124나라의 숫자
# n이 5억이기에 로직상 체크를 5억번할 수 있으므로
# 아래풀이 처럼 O(n)로는 풀면 안됨! 다른 규칙을 찾거나 해야함함
# 요세푸스와 비슷한 논리임, 1,2,4 뺑뺑이 도는 거

# 방법1) https://velog.io/@eerang/PYTHON-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2-124%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90
arr=['1','2','4']
def solution(n):
    answer=''
    while n>0:
        n-=1 # arr 인덱스는 0부터니까
        answer=arr[n%3]+answer # arr길이가 3이니까 3씩 나누기
        n//=3
    return answer

# 방법2) https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90-in-python
def solution2(n):
    if n<=3:
        return '124'[n-1]
    else:
        a,b = divmod(n-1,3) # n-1과 3의 몫과 나머지 도출
        return solution2(a)+'124'[b]

# 중복순열 구하는 함수 이용(효율성 X)
# from itertools import product
# arr=['1','2','4']
# def solution(n):
#     answer = []
#     cnt = 1
#     while 1:
#         for i in list(product(arr,repeat=cnt)): # procuct( ,cnt) : cnt길이의 중복순열 생성
#             answer.append(''.join(i))
#             if len(answer)>=n:
#                 break
#         else:
#             cnt+=1
#             continue
#         break
#     answer=sorted(answer)
#
#     return answer[-1]

