#10430 
a,b,c = map(int,input().split())
A= (a+b)%c
B= ((a%c)+(b%c))%c
C=(a*b)%c
D=((a%c)*(b%c))%c
print(A,B,C,D,sep='\n')

# 나누기
# /:나누기
# //: 몫
# % : 나머지
