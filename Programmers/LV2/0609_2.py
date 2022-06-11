# 괄호변환

def recur(s): # 재귀되는 부분
    hash = {'(': ')', ')': '('}
    res=''

    if len(s)==0:
        return ''

    u,v=fun_split(s)
    if check(u): # step 3
        res+=u+recur(v)
    else:       # step 4 : '(' + v의 재귀값 + ')' + 남은 u문자열을 올바른 괄호로 변환한 값
        temp='('
        temp+=recur(v)
        temp+=')'
        u= u[1:-1] # 첫번째 문자와 마지막 문자 제거
        for i in u:
            temp+=hash[i]
        res+=temp

    return res

def check(s): # 올바른 괄호인가
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    return False

def fun_split(s): # 두 문자열로 나누기
    s1,s2=0,0
    for i in range(len(s)):
        if s[i]=='(':
            s1+=1
        else:
            s2+=1

        if s1!=0 and s1==s2:
            if i+1<len(s):
                return s[:i+1],s[i+1:]
            else:
                return s,''

def solution(p):
    if check(p):
        return p
    answer=recur(p)
    return answer
