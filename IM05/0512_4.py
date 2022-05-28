# 10158 개미
# x축,y축 각각 생각해보면 x축 왔다갔다, y축 왔다갔다 하는거임
# https://kthng.tistory.com/29 그림 참고...이해부족
m,n=map(int,input().split())
x,y=map(int,input().split())
t=int(input())
x+=t # t만큼 더해진 위치
y+=t
x%=2*m # 2*m=x의 싸이클 주기 / => x%(2*m) 는 x축 위에서 현재 개미가 간 거리
y%=2*n
if x>m : # m보다 크다 : m지점을 지난 뒤부턴 반대방향으로(반사된 방향) 거미가 가는것
    x=2*m-x  # 개미의 위치
if y>n:
    y=2*n -y

print(f'{x} {y}')

# # 단순이동(2차원 배열)으로 풀 경우 시간 초과됨!
# m,n=map(int,in.txt().split())
# arr= [ [0]*m for i in range(n)]
# x,y=map(int,in.txt().split())
# t=int(in.txt())
#
# d=[(1,1),(1,-1),(-1,-1)] # 오위 왼위 왼아
# dir_arr=[0,1,2,1,0]
# dir=0
# while t>0:
#     y+=d[dir_arr[dir]][0]
#     x+=d[dir_arr[dir]][1]
#     if x<0 or x>m or y<0 or y>n:
#         y -= d[dir_arr[dir]][0]
#         x -= d[dir_arr[dir]][1]
#         dir=(dir+1)%5
#     else:
#         t-=1
# print(f'{x} {y}')




