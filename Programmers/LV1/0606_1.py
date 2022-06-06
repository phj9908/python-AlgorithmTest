# 자연수 뒤집어 배열로 만들기( 다시풀기 )
def solution(n): # n=12345
    n = str(n)
    n = n[::-1] # n=reversed(n)

    return list(map(int,n)) # ['5','4','3','2','1'] -> [5,4,3,2,1]로 빠르게 변환하는 방법