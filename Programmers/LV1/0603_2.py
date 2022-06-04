# 키패드 누르기
from collections import deque

def solution(numbers, hand):
    answer = ''
    numbers=deque(numbers)
    l_hand,r_hand=[],[]
    key={0:(3,1),1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

    while numbers:
        x=numbers.popleft()
        if str(x) in '147':
            l_hand.append(x)
            answer+='L'
        elif str(x) in '369':
            r_hand.append(x)
            answer+='R'
        else:
            ky,kx=key[x][0],key[x][1]
            if l_hand:
                ly,lx=key[l_hand[-1]][0],key[l_hand[-1]][1]
            else:
                ly,lx=3,0
            if r_hand:
                ry, rx = key[r_hand[-1]][0], key[r_hand[-1]][1]
            else:
                ry, rx = 3, 2

            if abs(ly-ky)+abs(lx-kx)>abs(ry-ky)+abs(rx-kx):
                r_hand.append(x)
                answer+='R'
            elif abs(ly-ky)+abs(lx-kx)<abs(ry-ky)+abs(rx-kx):
                l_hand.append(x)
                answer+='L'
            else:
                if hand=='left':
                    l_hand.append(x)
                    answer+='L'
                else:
                    r_hand.append(x)
                    answer+='R'

    return answer
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))