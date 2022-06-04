#숫자 문자열과 영단어
# replace(): 연속되는 문자열 처리시 유용

def solution(s):
    str_nums={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    for i in str_nums.items(): # key,value둘다 탐색
        s=s.replace(i[0],str(i[1])) # s에 i[0]부분이 있다면 str(i[1])로 바꾸기 / replace(바꾸고 싶은 부분, 바꿀 문자)
    
    return int(s)
