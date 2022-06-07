# 멀쩡한 사각형
# w,h 각각 1억 이하기에 규칙을 찾아내야함
# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def solution(w,h):
    g=gcd(w,h) # 최대공약수 = 잘라지는 박스들 덩어리 갯수
    slice_box=((w//g)+(h//g)-1)
    return (w*h)-g*slice_box