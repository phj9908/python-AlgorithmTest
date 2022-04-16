# 3499. 퍼펙트 셔플
from collections import deque

tc= int(input())
for t in range(1,tc+1):
    n=int(input())
    word=list(input().split())
    if len(word)%2==0:
        mid=len(word)//2
    else:
        mid=len(word)//2+1
    word_a=deque(word[:mid])    
    word_b=deque(word[mid:])
    
    word=[]
    while 1:
        if len(word_a)==0 and len(word_b)==0:
            break
        if word_a:
            word.append(word_a.popleft())
        if word_b:
            word.append(word_b.popleft())
        
    print(f'#{t}',end=' ');print(*word)
