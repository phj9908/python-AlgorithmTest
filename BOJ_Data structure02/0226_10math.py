#2089: -2진수
# -13 = -2*7 +1 / 7=-2*-3 +1/ -3 = -2*2 +1 / 2  = -2*-1 +0 / -1 = -2*1 +1 / 1 = -2*0 +1 => 뒤에서 부터 나머지값 모으면 110111
# -2로 n계속 나누기
# 나머지가 0 or 1
# 나머지가 1 일 땐 몫에 +1,나머지는 1로 처리
# 나머지가 0일땐 몫,나머지 그대로

n=int(input())
res=''
if n==0:
    print(0)
    exit() # 프로그랩 종료
while n!=0 :
    if n%-2: # n이 -2로 나눠떨어지지 않을때
        n=n//-2 +1
        res='1'+res
    else:
        n//=-2
        res='0'+res

print(int(res))


# 참고
# //연산자는 몫을 내림연산함. 7//-2 = -4, -3.5를 내림연산해서 -4
# %연산자는 x%y 연산에서 y의 부호를 따라감.