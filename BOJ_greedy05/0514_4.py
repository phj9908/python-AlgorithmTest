# 20115 에너지 드링크
from collections import deque

n=int(input())
arr=list(map(int,input().split()))
arr=deque(sorted(arr,reverse=True))
x=deque()
while arr:
    if len(x)==0:
        x.append(float(arr.popleft())+(arr.pop()/2))
    else:
        x.append(float(x.popleft())+(arr.pop()/2))

if x[0].is_integer(): # float이 정수인지 확인 (ex) 20.0
    print(int(x[0]))
else:
    print(x[0])




