# 주식가격

from collections import deque

def solution(prices):
    
    prices=deque(prices)
    answer = []
    cnt=0
    while prices:
        p=prices.popleft()  # 동일 코드이면서 deque활용 안하고 .pop(0)쓰는  경우 효율성 테스트 시간초과
        
        for i in prices:
            cnt+=1
            if i<p:
                break
            
        answer.append(cnt)
        cnt=0
    return answer

# 다른 풀이(처리시간 더 빠름) # for문 이해안감
#https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python

# def solution(prices):
#     length = len(prices)
    
#     # answer을 max값으로 초기화  prices = [1, 2, 3, 2, 3, 1]일 경우 answer = [5, 4, 3, 2, 1, 0]
#     answer = [ i for i in range (length - 1, -1, -1)]
    
#     # 주식 가격이 떨어질 경우 찾기
#     stack = [0]
#     for i in range (1, length):
#         print(i,stack)
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             answer[j] = i - j
#             print(i,j,stack)
#         stack.append(i)
#     return answer