def solution(atmos):
    answer = 0
    wear=0
    for a,b in atmos:
        if wear==0:
            if a>80 or b>35:
                if a<=150 or b<=75:
                    wear+=1
                answer += 1
        elif wear==1:
            if 150>=a>80 or 75>=b>35:
                wear+=1
            else:
                wear=0
        else:
            wear=0

    return answer
print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))