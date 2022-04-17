# (백준 1439)문자열 뒤집기
import math

n=input()
start=[]
answer=0
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        start.append(i)
    
if len(start)%2==0:
    answer=len(start)//2
else:
    answer=math.ceil(len(start)/2)
print(answer)