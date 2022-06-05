# 핸드폰 번호 가리기
def solution(phone_number):
    phone_number=list(phone_number) # 문자열 슬라이싱한 거를 다른 문자열에 할당하려면 list()로 변환하기
    phone_number[:-4]='*'*(len(phone_number)-4)
    return ''.join(phone_number)

# 문자열 그대로 바로 하는 방법
# return '*'*(len(s)-4)+s[-4:]