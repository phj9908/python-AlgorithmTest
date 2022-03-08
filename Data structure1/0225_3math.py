#2609
#최대공약수(Greatest Common Divisor) -> 유클리드 호제법
#최소공배수(Least Common Multiple) -> 최대공약수 함수 이용
a,b = map(int,input().split())
A,B=a,b
while b!=0 : # b가 0이 될때의 a값이 최대공약수
    a = a%b
    a,b = b,a
    
print(a) #gcd
print(A*B//a) # lcm # 최소공배수 = 기존의 수 // 최대공약수

