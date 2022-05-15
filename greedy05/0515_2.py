# 16953 A->B
import sys

def recur(a,b,cnt):
    global answer
    if a==b:
        answer=min(answer,cnt+1)
        return
    if a>b:
        return

    recur(a*2,b,cnt+1)
    recur(int(str(a)+'1'),b,cnt+1)

a,b=map(int,input().split())
answer=sys.maxsize
recur(a,b,0)
if answer!=sys.maxsize:
    print(answer)
else:
    print(-1)
