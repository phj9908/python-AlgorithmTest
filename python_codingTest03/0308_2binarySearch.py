#정렬된!! 배열에서 특정수의 갯수 구하기
# O(logN)의 시간복잡도로 설계해야함. 선형 탐색으로 하면 시간초과
# 파이썬 내장함수 bisect_left,bisect_right를 이용하여 특정값이 존재하는 첫 위치와 마지막 위치간 차 이용

from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
arr= list(map(int,input().split()))

def count_by_range(arr,left_val,right_val): 
    left_idx=bisect_left(arr,left_val) # arr의 중간점 기중 왼쪽에서 left_val의 첫 인덱스 값 반환
    right_idx=bisect_right(arr,right_val)

    return right_idx-left_idx # 값이 [left_val,right_val]인 데이터 갯수 반환

cnt= count_by_range(arr,x,x)
if cnt==0:
    print(-1)
else:
    print(cnt)
