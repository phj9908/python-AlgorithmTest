# 가운데 글자 가져오기
def solution(s):

    if len(s)%2==0:
        return ''.join(s[len(s)//2-1:len(s)//2+1])
    return s[len(s)//2]