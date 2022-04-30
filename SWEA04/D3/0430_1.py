# 5607. [Professional] 조합(이해 부족)
# https://rhdtka21.tistory.com/123 참고
# 큰 수끼리 나누기가 불가하여 combination의 나눗셈을 곱셈연산으로 바꿔야함>> 페르마의 소정리 이용

def power(a,b):
    if b==0:
        return 1
    if b%2: # b가 홀수면
        return (power(a,b//2)**2*a)%p
    else:
        return (power(a,b//2)**2)%p

p=1234567891
for t in range(1,int(input())+1):
    n,r=map(int,input().split())
    dp=[ i for i in range(n+1)]    
    for i in range(2,n+1):
        dp[i]=i*dp[i-1]%p
    A=dp[n]
    B=(dp[n-r]*dp[r])%p
    answer=(A%p)*(power(B,p-2)%p)%p

    print(f'#{t} {answer}')