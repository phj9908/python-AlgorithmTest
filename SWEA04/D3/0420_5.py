# 신뢰(다시풀어보기)
# https://colinder.github.io/sw_21.01.04/ 코드 참고
from collections import deque

tc=int(input())
for t in range(1,tc+1):
    arr=deque(input().split())
    n=arr.popleft()

    B_arr=deque()
    O_arr=deque()
    command=deque()
    while arr:
        i = arr.popleft()
        if i=='B':
            B_arr.append(int(arr.popleft())) # B가 누를 버튼 숫자 할당
            command.append('B')
        else:
            O_arr.append(int(arr.popleft()))
            command.append('O')

    cnt=0
    b,o=1,1 # 시작 위치
    while command:
        cnt+=1
        btn_press=False # 버튼을 동시에만 누르면 안되니까 False로 초기화를 while문에서 반복해도 됨

        if B_arr:
            if B_arr[0]>b: # B의 버튼 중에 가장 가까운버튼까지 더 가야할 때
                b+=1
            elif B_arr[0] == b and command[0]=='B':
                B_arr.popleft()
                command.popleft()
                btn_press=True
            elif B_arr[0]<b:
                b-=1
        if O_arr:
            if O_arr[0]>o:
                o+=1
            elif O_arr==o and command[0]=='0' and btn_press==False:
                O_arr.popleft()
                command.popleft()
            elif O_arr[0]<o:
                o-=1

    print(f'#{t} {cnt}')


