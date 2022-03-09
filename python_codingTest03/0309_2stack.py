#스택 함수 구현

stack_size=3 # 스캑 크기 제한

class Stack: # class 첫 글자는 대문자

    def __init__(self): # 매개변수 없는 생성자
        self.arr=[None]*stack_size
        self.top=-1

    def is_full(self):
        if self.top>=stack_size-1:
            return True
        else:
            return False

    def push(self,value):
        if self.is_full():
            print('스택이 가득 찼습니다.')
        else:
            self.top+=1
            self.arr[self.top]=value # = arr.append(value)
    def is_empty(self):
        if self.top<0:
            return True
        else:
            return False

    def pop(self):
        if(self.is_empty()):
            print('스택이 비어있습니다.')
        else:
            value=self.arr[self.top]
            self.top-=1
            return value
            
stack=Stack()
stack.push(1)
stack.push(2)
print('pop:',stack.pop())
    