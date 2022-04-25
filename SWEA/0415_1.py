# 3142. 영준이와 신비한 뿔의 숲
tc= int(input())
for t in range(1,tc+1):
    n,m=map(int,input().split())
    
    y = 2*m-n # x+y=m ,2*x+y=n 연립방정식
    x = m-y
    print(f'#{t} {y} {x}')
