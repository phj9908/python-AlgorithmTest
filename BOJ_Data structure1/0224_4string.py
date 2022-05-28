#10820 문자열 분석
#is~() 메서드 활용
#문제에서 몇개의 테스트케이스가 주어지는지 제한하지 않아서, EOF검사 해야함-> sys.stdin.readline()으로 입력 여부 파악
# in.txt()사용할 경우 try-except로 EOFErorr처리

import sys

while 1:
    str= sys.stdin.readline().rstrip('\n') # 입력 끝의 \n만 제거
    up,lo,num,null =0,0,0,0

    if not str: # 입력이 없다면
        break
    for i in str:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
        elif i.isdigit():
            num +=1
        elif i.isspace():
            null +=1
    sys.stdout.write('{} {} {} {}\n'.format(lo,up,num,null))
