 # 3029 경고( 다시풀기. 20:00:00~ 04:00:00 의 시계 그림그리면 코드이해함 )
h1,m1,s1= map(int,input().split(':')) # start
h2,m2,s2=map(int,input().split(':')) # end
t1= h1*3600+m1*60+s1
t2= h2*3600+m2*60+s2
if t1>t2:
    total=t2-t1+24*3600
else:
    total=t2-t1
h=total//3600
m=(total%3600)//60
s=total%60
print('%02d:%02d:%02d'%(h,m,s)) # 08:00:00
# print('{:02d}:{:02d}:{:02d}'.format(h,m,s)) # 08:00:00
