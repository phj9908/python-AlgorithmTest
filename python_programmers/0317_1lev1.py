#숫자 문자열과 영단어
# replace(): 연속되는 문자열 처리시 유용

def solution(s):
    str_nums={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    for i in str_nums.items(): # key,value둘다 탐색
        s=s.replace(i[0],str(i[1])) # s의 i[0]부분을 str(i[1])로 변환
    
    return int(s)

# #원래 내 풀이
# def solution(s):

#     eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     if s.isdigit():
#         return int(s) # 바로리턴 

#     answer = ''
#     temp = ''
#     for i in s:
#         if i.isdigit():
#             answer+=i
#         # 문자열이면 
#         else:
#             temp += i
#             if temp in eng:
#                 answer += str(eng.index(temp))
#                 temp = ''

#     #print(answer)   
#     return int(answer)
