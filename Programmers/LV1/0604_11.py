# 2016년(윤년)

d = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arr = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']


def solution(a, b):
    if a == 1:
        return arr[(b - 1) % 7]
    else:
        day = b
        for i in range(1, a):
            day += d[i - 1]
        answer = arr[(day - 1) % 7] # 시작이 (1월)1일 이니까 day -1

    return answer