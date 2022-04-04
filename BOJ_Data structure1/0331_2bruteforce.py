# 6064 카잉 달력
# x,y가 1씩 증가하면서 최댓값(x 최댓값은 M, y최댓값은 N)에 도달하면 1로 돌아가는 순환로직
# 마지막해는 자연스럽게 x,y의 최소공배수
# 문제 이해.. https://dirmathfl.tistory.com/113
# x,y 둘다 x'=x+1,y'=y+1인데 왜 N으로만 나누고 x만 +M 증가시키는지 ???

n=int(input())

for _ in range(n):
    m,n,x,y=map(int,input().split())
    while x<=m*n: # 최소공배수 함수쓰면 시간초과해서 그냥 m*n
        if x%n == y%n:
            print(x)
            break
        x+=m
    else:
        print(-1)