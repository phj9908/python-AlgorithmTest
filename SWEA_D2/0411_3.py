# 1940 가랏 Rc카
tc=int(input())
for t in range(1,tc+1):
    number=int(input())
    arr=[]
    for _ in range(number):
        x=input()
        if ' ' in x:
            num,speed=map(int,x.split())
            arr.append((num,speed))
        else:
            arr.append((0,0))
    
    answer=0
    vel=0 # velocity : 속도
    sec=0

    while len(arr)!=0:
        num,speed = arr.pop(0)
        if num==1:
            vel+=speed
        elif num==2:
            if abs(vel)<speed: # 문제 조건으로, 현재속도보다 감속할 속도가 더 틀 경우
                speed=0 # 속도는 0이 된다
            vel-=speed
        answer+=abs(vel)
    print(f'#{t} {answer}')
            
