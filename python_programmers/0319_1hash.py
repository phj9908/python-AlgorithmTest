# 베스트 앨범: 총 플레이 횟수에 따라 장르별로 인덱스 각각 내림차순 정렬

def solution(genres,plays):
    answer=[]

    table={}     # {장르:[(플레이횟수,고유 번호)]}
    sum_table={} # {장르: 총 재생횟수 }
    
    # 해시 테이블 초기화
    for i in range(len(genres)):
        table[genres[i]]=table.get(genres[i],[])+[(plays[i],i)]
        sum_table[genres[i]]=sum_table.get(genres[i],0) +plays[i]

    # 재생횟수 합 내림차순으로 장르별 정렬
    genres_sorted=sorted(sum_table.items(),key=lambda x:x[1],reverse=True) # x[0]:key,x[1]:value

    for genre,total_play in genres_sorted:
        table[genre]= sorted(table[genre],key=lambda x: (-x[0],x[1])) # 재생횟수 내림차순, 인덱스 오름차순 정렬(장르내에서 재생횟수가 같으면 고유번호가 낮은 순으로 정렬)

        answer +=[idx for play,idx in table[genre][:2]] # 한 장르내에서 고유번호 2개까지 출력

    return answer
