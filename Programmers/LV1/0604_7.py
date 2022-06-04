# 약수의 개수와 덧셈
# 참고 : 제곱수의 약수의 갯수는 홀수개이고 , 그 외의 수는 약수의 갯수가 짝수개이다

def fun(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        x=fun(i)
        if x%2==0:
            answer+=i
        else:
            answer-=i
    return answer