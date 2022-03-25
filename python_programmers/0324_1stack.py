#후위표기식 연산

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c) # 숫자는 숫자의 형태로 리스트에 반환
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)    # 연산자나 괄호는 문자열의 형태로 반환
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList): # 중위 표현 수식을 후위 표기수식으로
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for i in tokenList:
        if i=='(':
            opStack.push(i)
        elif i==')':
            while opStack.peek()!='(': 
                postfixList.append(opStack.pop())
            opStack.pop() # 마지막 '(' pop
        elif i in prec:
            if not opStack.isEmpty() and prec[i]<=prec[opStack.peek()]: # opStack.pop()을 조건식에 적으면 인덱스에러 남
                while opStack:
                    postfixList.append(opStack.pop())
            opStack.push(i)
        else:
            postfixList.append(i)
            
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList): #후위표기식 연산
    opStack=ArrayStack()
    for i in tokenList:
        if type(i) is int:
            opStack.push(i)
        else:
            if opStack.size()>=2:
                num1=opStack.pop()
                num2=opStack.pop()
                if i=='*':
                    opStack.push(num1*num2)
                if i=='/':
                    opStack.push(num2/num1)
                if i=='+':
                    opStack.push(num1+num2)
                if i=='-':
                    opStack.push(num2-num1)
    if not opStack.isEmpty():
        val=opStack.pop()
    return val


def solution(expr):
    tokens = splitTokens(expr) 
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

str= input()
print(solution(str))
