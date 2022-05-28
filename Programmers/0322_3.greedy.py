# 단속 카메라

def solution(routes):

    answer=0
    routes.sort(key= lambda x:x[1]) # 진출 시점 기준 정렬
    camera=-30001 ## 문제 제한 사항 중 차량의 최소 진입지점이 -30000

    for route in routes: 
        if camera<route[0]: # 카메라가 해당 루트 진입접 밖에 위치할 때
            answer+=1   # 카메라 추가 설치
            camera=route[1]     # 해당 루트 진출점으로 카메라 위치 갱신(진출점으로 지정해야 다음 루트의 진입점 위치 비교하기 용이하니까)
    return answer