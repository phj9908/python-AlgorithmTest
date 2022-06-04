# 예산
def solution(d, budget):
    d=sorted(d)
    for i in range(len(d)):
        budget-=d[i]
        if budget<0:
            answer=i
            break
    else:
        return len(d)
    return answer
