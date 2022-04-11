# 1946 간단한 압축 풀기

import math

tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    alpha_arr=[]
    sum=0
    for _ in range(n):
        x,num=input().split()
        [ alpha_arr.append(x) for _ in range(int(num)) ]
        sum+=int(num)
    row=math.ceil(sum/10)

    arr=[ ['']*10 for i in range(row)]
    row=0

    while len(alpha_arr)!=0:
        for i in range(10):
            if len(alpha_arr) !=0:
                arr[row][i]=alpha_arr.pop(0)
        row+=1
        
    print(f'#{t}')
    for i in arr:
        print(''.join(i))

# 다른 풀이
# 문자열 변수 하나에 입력할 문자열 싹 넣은뒤 길이 10만큼 잘라 출력
# T = int(input())
# for tc in range(1, 1+T):
#     n = int(input())
#     arr = ''
#     for _ in range(n):
#         word, number = input().split()
#         arr += word*int(number)

#     print(f'#{t}')
#     for i in range(0, len(document), 10):
#         print(document[i:i+10])