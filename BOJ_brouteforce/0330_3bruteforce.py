# 날짜계산 # 세 수의 나머지가 모두 0이 되는 연도 찾기

y1,y2,y3 = map(int,input().split())
year=1
while True:
    if (year-y1)%15==0 and (year-y2)%28 ==0 and (year-y3)%19==0:
        break
    year +=1
print(year)

# 내 풀이, 너무 복잡하게 풀었다..더 빠르긴 함
# a,b,c=map(int,in.txt().split())
# cnt=[0]*3
# n=[0]*3
# while True:
#     n[0]=15*cnt[0]+a
#     n[1]=28*cnt[1]+b
#     n[2]=19*cnt[2]+c

#     if n[0]==n[1]==n[2]:
#         break
#     elif n.count(max(n))==1:
#         for i,j in enumerate(n):
#             if j!=max(n):
#                 cnt[i]+=1
#     elif n.count(max(n))==2:
#         i=n.index(min(n))
#         cnt[i]+=1
# print(n[0])
        