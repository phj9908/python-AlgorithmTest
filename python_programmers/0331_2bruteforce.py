# 6064 카잉 달력
# x,y가 1씩 증가하면서 최댓값에 도달하면 1로 돌아가는 순환로직
# 마지막해는 자연스럽게 x,y의 최소공배수가 됨
# 문제 이해.. https://dirmathfl.tistory.com/113


def num(m,n,x,y):
    while x<m*n: # 마지막 해인 최소공배수까지 하면 더 좋지만 최소공배수까지 구하면 시간초과
        if (x-y)%n==0:
            return x
        x +=m
    return -1

n = int(input())
for i in range(n):
    m,n,x,y = map(int,input().split())
    print(num(m,n,x,y))