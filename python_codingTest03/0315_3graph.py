# 그래프 : 여러개의 정점과 그 정점들을 잇는 간선으로 이뤄짐(간선의 방향유무에 따라,가중치가 존재하는지에 따라 종류가 나뉨)
# 2가지 방식 : 인접 행렬(2차원 배열) / 인접리스트(링크드 리스트 이용)
# 인접행렬 방식은 메모리 효율이 안좋기에 노드 수가 적고 간선 수가 많은 밀집 그래프에 적합
# 인접 리스트 방식은 노드를 탐색할 때 시간 효율이 안좋기에 노드 수가 많고 간선의 수가 적은 희소 그래프에 적합

# 인접 행렬 그래프에서 데이터 삽입

arr=[[0]*4 for _ in range(4)] # 4X4의 행렬 생성

def insert(put_node,get_node,num,not_vector): # 주는 노드, 받는 노드, 가중치, 무방향 그래프 여부
    if not_vector:
        arr[put_node][get_node]+=num
        arr[get_node][put_node]+=num
    else:
        arr[put_node][get_node]+=num
    
insert(0,1,1,1)
insert(0,3,1,1)
insert(1,2,1,1)
insert(1,3,1,1)
insert(2,3,1,1)

for i in range(4):
    print(*arr[i])