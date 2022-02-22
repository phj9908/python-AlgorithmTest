import sys

str = sys.stdin.readline().strip()
stack=[]
ans=0
for i in range(len(str)):
    if str[i] =='(':
        stack.append('(')
    else:
        stack.pop()
        if str[i-1]=='(':
            ans+=len(stack)
        else :              #'))'일 때 : 쇠막대기 끄트머리 표현
            ans +=1
print(ans)




