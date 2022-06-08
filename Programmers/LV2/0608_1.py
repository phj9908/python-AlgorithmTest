# 짝지어 제거하기
# stack 이용
def solution(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        return 1
    return 0

# replace 이용 : 실패 (시간초과는 아님)
def solution(s):
    set_s = set(s)

    for i in set_s:
        if i * 2 in s:
            s=s.replace(i * 2, '')
            print(s)

    return 1 if s=='' else 0