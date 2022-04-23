# 정렬된 배열에서 특정 수의 개수 구하기(다시풀기)

# 내장함수 bisect 활용 ver
from bisect import bisect_left,bisect_right

n,x=map(int,input().split())
arr=list(map(int,input().split()))

def count(left_num,right_num):
    left_idx=bisect_left(arr,left_num)
    right_idx=bisect_right(arr,right_num)

    return right_idx-left_idx

if x not in arr:
    print(-1)
else:
    print(count(x,x)) 

# 이분탐색 ver
