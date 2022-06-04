# 3진법 뒤집기
def solution(n):
    answer = 0
    ans=''
    while n>0: # n>3 했다가 일부 테케 실패.. 주의!
        ans+=str(n%3)
        n//=3
    ans=ans[::-1]
    for i in range(len(ans)):
        answer+=(3**i)*int(ans[i])

    return answer