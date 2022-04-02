# 1918 : 중위표기식을 후위표기식으로 나타내기, 연산자를 스택에 저장
# 우선순위 *,/는 push, 그다음 우선순위 +-는 stack의 '('까지 연산자를 pop한뒤 push,'('없으면 스택 끝까지
# 후위표기식으로 나타내기 순서 https://reakwon.tistory.com/62
# 다시 풀어보기

str = input()
result=[]
stack=[] 

for i in str:
    if i.isalpha():
        result.append(i)
    elif i =='*' or i == '/':
        while stack and (stack[-1]=='*' or stack[-1] =='/'): # ex) A*B*C
            result.append(stack.pop())
        stack.append(i)
    elif i == '+' or i=='-':
        while stack and stack[-1] != '(':
                result.append(stack.pop())  
        stack.append(i)
    elif i ==')':
        while stack and stack[-1] != '(':
            result.append(stack.pop()) 
        stack.pop() # 스택의 '('pop
    else : # (
        stack.append(i)
while stack:
    result.append(stack.pop())

print(''.join(result)) 
