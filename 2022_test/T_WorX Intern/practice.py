def solution(p):
    answer = [0]*len(p)
    for i in range(len(p)-1):
        min_idx=p.index(min(p[i+1:]))
        if p[i]> p[min_idx]:
            answer[min_idx] += 1
            answer[i]+=1
            p[i], p[min_idx] = p[min_idx], p[i]

    return answer
print(solution([2,5,3,1,4]))