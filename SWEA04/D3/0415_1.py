# 3142. 영준이와 신비한 뿔의 숲
tc= int(input())
for t in range(1,tc+1):
    n,m=map(int,input().split())
    
    x=n-m # x+y=m ,2*x+y=n 연립방정식
    y=m-x
    print(f'#{t} {y} {x}')
