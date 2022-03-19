# 완주하지 못한 선수 : 참가자 목록과 완주자 목록을 비교하여 , 완주하지 못한 선수 1명 찾기(단,동명이인 있을 수 있음)
# hash이용

def solution(particiation,completion):
    hash_table={} # 해쉬 테이블 생성 (주의!!! {}!!!중괄호!!!)

    for i in particiation:
        hash_table[i]=hash_table.get(i,0)+1 # get(key,defalut): 만약 key가 리스트에 없다면 defalut값 리턴)i가 처음 등장하면 1로 만들고, 그게 아니면 원래있던 값에 1더하기
    for i in completion:
        hash_table[i] -=1       # particiaion의 동일한 이름나오면 -1(같은 key 등장 시 값에서 -1) ==> 결국 미완주자 한명 key의 value값은 1이 됨
    
    for k,v in hash_table.items():
        if v>0:
            answer=k
    return answer

# # 다른 풀이1(딕셔너리 이용)
# import collections

# def solution(participant,completion):
#     answer= collections.Counter(participant)-collections.Counter(completion)
#     return list(answer.keys())[0]

# # 다른 풀이2(sort()이용)
# def solution(participant,completion):
#     participant.sort()
#     completion.sort()
#     for p, c in zip(participant,completion):
#         if p!=c:
#             return p           # 같지않은 값이 나오면 바로 멈춰 미완주자 이름 도출
#     return participant[-1]     # for문을 돌고도 미완주자를 못찾았을 때, 마지막 사람이 미완주자가 됨(completion보다 participant가 한명더 많으니)