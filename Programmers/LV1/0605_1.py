# 나머지가 1이되는 수 찾기
def solution(n):

    cnt=2
    while 1:
        if n%cnt==1:
            break
        cnt+=1
    return cnt