#로또의 최고순위와 최저순위
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 등수 미리 배열로 저장

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans] # ex) [1,6]