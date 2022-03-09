#스택: 괄호 판정

def validate_barace_pair(arr):
    stack=[]
    for i in arr:
        if i == '{':
            stack.append('{')
        else:
            if stack:
                stack.pop()
            else:
                print('유효하지 않은 중괄호 쌍입니다.')
                return
    if stack:
        print('유효하지 않은 중괄호 쌍입니다.')
    else :
        print('유효한 중괄호 쌍입니다.')
validate_barace_pair('{}{}{')
