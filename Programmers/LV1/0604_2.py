# 없는 숫자 더하기
arr=[ i for i in range(10)]
def solution(numbers):
    answer = 0
    for i in arr:
        if i not in numbers:
            answer+=i
    return answer