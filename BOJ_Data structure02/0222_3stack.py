# 10799 쇠막대기 (다시 풁어보기)
import sys

str = sys.stdin.readline().strip()
stack=[]
ans=0
for i in range(len(str)):
    if str[i] =='(':
        stack.append('(')
    else:
        stack.pop()
        if str[i-1]=='(': # 주의! stack[i-1]이 아니고 str[i-1]임!!
            ans+=len(stack)
        else :              #'))'일 때 : 쇠막대기 끄트머리 표현
            ans +=1
print(ans)




