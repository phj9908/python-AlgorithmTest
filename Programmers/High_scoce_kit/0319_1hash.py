# 베스트 앨범: 총 플레이 횟수에 따라 장르별로 인덱스 각각 내림차순 정렬
 

def solution(genres, plays):
    answer = []

    dic1={} # (고유번호, 플레이 수) 할당
    dic2={} # 플레이수 총합 할당

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): 
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
