# 신규 아이디 추천

def solution(new_id):

    answer=''
    #1단계
    new_id = new_id.lower()

    #2단계
    for i in new_id:
        if i.isalnum() or i in '-_.': # i가 '-_.'내에 하나라면 or 알파벳이나 숫자면
            answer+=i
    
    #3단계 : .가 연속 2개이상이면 .하나로 대체
    while '..' in answer:
        answer = answer.replace('..','.')

    #4단계
    answer = answer[1:] if answer[0]=='.' and len(answer)>1 else answer
    answer = answer[:-1] if answer[-1]=='.' else answer #answer[:-1]:마지막 문자만 제외

    #5단계
    answer = 'a' if answer ==''  else answer  

    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7단계
    while len(answer)  <3:
        answer +=answer[-1]
    
    return answer

# 정규식표현을 이용한 더 쉬운 문자열 교체방법
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)  # st중에 알파벳,숫자,-_.외의 문자는 ''로 만듦
#     st = re.sub('\.+', '.', st) # st문자 중에 .이 연속으로 있는 부분은 .로 만듦
#     st = re.sub('^[.]|[.]$', '', st) # st의 맨 앞과 맨 뒤의 문자가 .일땐 ''로 만듦
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st