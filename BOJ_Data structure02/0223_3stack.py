# 1935 후위표기식2, 후위표기식을 연산, 숫자를 스택에 할당
# 후위표기식 개념 https://simsim231.tistory.com/54
# 다시풀어보기

n = int(input())
str = input()
nums=[] # 피연산자에 해당하는 숫자 저장

for i in range(n):
    nums.append(int(input()))

stack=[] 

for word in str:
    if word.isalpha():
        stack.append(nums[ord(word)-ord('A')]) # A면 stack[0]에 nums[0]할당, C면 stack[2]에 nums[2]할당...
    else :
        num1=stack.pop()
        num2=stack.pop()
        
        if word =='+':
            stack.append(num1+num2)
        elif word =='-':
            stack.append(num2-num1)
        elif word == '*':
            stack.append(num1*num2)
        elif word =='/':
            stack.append(num2/num1)

print('%.2f'%stack[0]) # 연산을 마친 값은 최종적으로 stack[0]이 됨
