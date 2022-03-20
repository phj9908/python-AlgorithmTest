#구명보트
# 사람들 몸무게를 오름차순 정렬 한뒤, 가장 큰 사람과 가장 작은 사암의 값을 더해 limit값보다 작으면 둘다 태우고 크면 가장 큰사람만 태움

# 인덱싱 이용
def solution(people,limit):
    cnt=0
    people.sort()
    min=0
    max=len(people)-1

    while min<=max:
        cnt+=1
        if people[min]+people[max]<=limit:
            min+=1
        max-=1
    return cnt



# # 다른 풀이(deque)
# from collections import deque

# def solution(people,limit):
    
#     p =deque(sorted(people))

#     answer=0

#     while p:
#         if len(p)==1:
#             return answer+1
#         if p[0]+p[-1]<=limit:
#             p.pop()
#             p.popleft()
#             answer+=1
#         elif p[0]+p[-1]>limit:
#             p.pop() # 큰 수 만 제거
#             answer+=1
#     return answer