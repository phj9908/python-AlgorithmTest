# 신고 결과 받기
# 내풀이
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    hash={id:0 for id in id_list}
    res_hash={id:[] for id in id_list}
    for r in list(set(report)):
        a,b=r.split()
        hash[b]+=1
        res_hash[a].append(b)

    for key,v in hash.items():
        if v>=k:
            break
    else:
        return answer

    for key,val in res_hash.items():
        for value in val:
            if hash[value]>=k:
                answer[id_list.index(key)]+=1

    return answer

# 더 간단하게 하는 방법
# 해시를 여러개 만들기보다 report부분을 쪼개면서 쓰기!!
#
# for r in set(report):
#     hash[r.split()[1]]+=1
#
# for r in set(report):
#     if reports[r.split()[1]]>=k:
#         answer[id_list.index(r.split()[0])]+=1