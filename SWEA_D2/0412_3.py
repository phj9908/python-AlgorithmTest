# 3431 준환이의 운동관리

tc=int(input())
for t in range(1,tc+1):
    l,u,x=map(int,input().split())
     
    if x>u:
        answer=-1
    else:
        if x<l:
            answer=l-x
        elif x>=l:
            answer=0
    
    print(f'#{t} {answer}')