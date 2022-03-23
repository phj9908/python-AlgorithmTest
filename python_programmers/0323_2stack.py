# 중위 표기법을 후위 표기법으로 변환

#왼쪽부터 피연산자면 그냥 출력
# (이면 스택에 push 
# )이면 (나올 때 까지 스택에서 pop,출력
# 연산자면 스택에서 이보다 높거나 같은 우선순위들을 pop, 출력 그리고 이 연산자는 스택에 push
# 끝까지 왔다면 스택에 남은 연산자들은 모두 pop, 출력

from xml.etree.ElementPath import ops


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for s in S:
        if s.isalpha():
            answer+=s
        if s=='(': 
                opStack.push(s)
        if s==')':  # 닫는 괄호를 만나면 
            while opStack and opStack.peek()!='(':     # 열린 괄호를 만날 때까지 
                answer+=opStack.pop()
            opStack.pop()   # 스택의 '(' pop
        else:      
            if not opStack.isEmpty(): # 그냥 if opStack:하면 인덱스 에러
                res=opStack.peek()
                if prec[s]<=prec[res]:  # 스택의 마지막 원소가 현재 연산자의 우선순위보다 높거나 같으면
                    while opStack:
                        answer+=opStack.pop()
            opStack.push(s)
                    
    while opStack:
        answer+= opStack.pop()
                    
    return answer