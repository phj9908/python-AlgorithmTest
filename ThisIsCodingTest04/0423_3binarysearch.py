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

# # 이분탐색 ver 함수 (고난도, 암기하는 느낌으로 참고)
# def count_by_value(arr,x):
#     n=len(arr) # 데이터 갯수
    
#     a=first(arr,x,0,n-1) # x가 처음 등장한 인덱스 계산
#     if a==None: # arr에 x가 없으면
#         return 0 

#     b=last(arr,x,0,n-1) # x가 마지막으로 등장한 인덱스

#     return b-a+1

# def first(arr,target,start,end):
#     if start>end:
#         return None
#     mid=(start+end)//2
#     if (mid==0 or target >arr[mid-1])and arr[mid]==target: # x값의 인덱스중 가장 왼쪽의 인덱스 반환
#         return mid
#     elif arr[mid]>=target:
#         return first(arr,target,start,mid-1)
#     else:
#         return first(arr,target,mid+1,end)

# def last(arr,target,start,end):
#     if start>end:
#         return None
#     mid=(start+end)//2
#     if (mid==n-1 or target<arr[mid-1]) and arr[mid]==target: # x값의 인덱스 중 가장 오른쪽의 인덱스 반환
#         return mid
#     elif arr[mid]>=target:
#         return last(arr,target,start,mid-1)
#     else:
#         return last(arr,target,mid+1,end)



    

