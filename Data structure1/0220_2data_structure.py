import sys

n = int(sys.stdin.readline())
for _ in range(n):
    arr = sys.stdin.readline().rstrip()
    pop_arr=[]
    for i in arr:
        if i == '(':
            pop_arr.append(')')
        else :
            if pop_arr : # =len(pop_arr) !=0 # arr= (((일때 err방지
                pop_arr.pop()
            else :
                print('NO')
                break
    else : # break으로 끊기지 않고 수행했을 경우
        if len(pop_arr) !=0:
            print('NO')   
        else :
            print('YES')