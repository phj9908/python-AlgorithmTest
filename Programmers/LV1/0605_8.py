# 다트게임
def solution(dartResult):
    answer = 0
    star=False
    for i in range(len(dartResult)-1,-1,-1):
        if dartResult[i].isalpha():
            if i-2>=0 and dartResult[i-2].isdigit():
                x=int(dartResult[i - 2:i])
            else:
                x = int(dartResult[i - 1])
            if dartResult[i]=='T':
                x**=3
            elif dartResult[i]=='D':
                x**=2

            if star:
                x*=2
                star=False

            if i+1<len(dartResult) and dartResult[i+1]=='*':
                x*=2
                star=True
            elif i+1<len(dartResult) and dartResult[i+1]=='#':
                x*=-1

            answer+=x

    return answer