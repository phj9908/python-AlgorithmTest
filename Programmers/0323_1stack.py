# 스택
# 괄호 판정

class ArrayStack:
    def __init__(self):
        self.arr=[]
    
    def size(self):
        return len(self.arr)
    
    def isEmpty(self):
        return self.size()==0

    def push(self,item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def peek(self): # 스택의 마지막 값 반환
        return self.arr[-1]
    
def solution(ex):

    match={         # key-value형태로 괄호들 저장
        ')':'(',
        '{':'}',
        '[':']'
    }

    S=ArrayStack()
    for i in ex:
        if i in'({[':
            S.push(i)
        elif i in match:
            if S.isEmpty():
                return False
            else:
                t= S.pop()
                if t!=i:
                    return False
    return S.isEmpty()  # for문을 다 돌고난 후 스택이 비었으면 괄호가 짝맞게 있던거고 안 비어있다면 짝이 안 맞는 거니까
