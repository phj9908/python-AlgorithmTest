# 다리를 지나는 트럭
# 다리를 1만큼 건널때 1초 소요됨!

def solution(bridge_length,weight,truck_weights):
    answer=0
    bridge=[0]*bridge_length    # 다리 길이와 같은 스택 생성
    bridge_weight=0 # 현재 다리위의 트럭 무게

    while bridge or bridge_weight>0:
        answer+=1   # 트럭이 다리 지나는 과정, 경과시간 계산
        removed_truck=bridge.pop(0)
        bridge_weight-=removed_truck
        
        if truck_weights:
            if bridge_weight+truck_weights[0]<=weight:
                truck=truck_weights.pop(0)
                bridge.append(truck)
                bridge_weight+=truck
            else:   # 트럭이 더 올라갈수 없을 때
                bridge.append(0)    # [0] 추가해서 다리길이 유지
    return answer

print(solution(2,10,[7,4,5,6]))