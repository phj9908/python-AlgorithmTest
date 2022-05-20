# 1918 : 중위표기식을 후위표기식으로 나타내기, 연산자를 스택에 저장
# 우선순위 *,/는 push, 그다음 우선순위 +-는 stack의 '('까지 연산자를 pop한뒤 push,'('없으면 스택 끝까지
# 후위표기식으로 나타내기 순서 https://reakwon.tistory.com/62
# 다시 풀어보기

str = input()
prec = {  # 연산자 우선순위
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = []
    answer = ''

    for s in S:
        if s.isalpha():
            answer += s
        if s == '(':
            opStack.append(s)
        if s == ')':  # 닫는 괄호를 만나면
            while opStack and opStack[-1] != '(':  # 열린 괄호를 만날 때까지
                answer += opStack.pop()
            opStack.pop()  # 스택의 '(' pop
        else: # 연산자
            if len(opStack)>0:  # 그냥 if opStack:하면 인덱스 에러
                res = opStack[-1]
                if prec[s] <= prec[res]:  # 스택의 마지막 원소가 현재 연산자의 우선순위보다 높거나 같으면
                    while opStack:
                        answer += opStack.pop()
            opStack.append(s)

    while opStack:
        answer += opStack.pop()

    return answer

print(''.join(solution(str)))