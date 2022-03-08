# 퀵정렬
# 최악의 경우 O(n^2), 평균 O(nlogn)의 시간 복잡도 가짐
# 크기의 기준이 되는 한 원소(pivot)를 잡아 놓고 피벗보다 작은 원소들만 모은 리스트, 큰 원소만 모은 리스트 생성해서 반복...
# 이코테 강의 참고

# 파이썬의 장점을 살린 간편한 방식
arr=list(map(int,input().split()))

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot =arr[0] # 피벗은 첫번째 원소로 지정
    tail=arr[1:]  # 피벗을 제외한 리스트 생성

    left_arr=[x for x in tail if x<pivot] # 피봇보다 작은 원소들 리스트 생성
    right_arr=[x for x in tail if x>pivot] 

    return quick_sort(left_arr)+ pivot + quick_sort(right_arr) # 재귀로 반복

print(quick_sort(arr))

# # 기존의 방식
# def quick___sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot = arr[0]  
#     left,right,mid=[],[],[]

#     for x in arr:
#         if x <pivot:
#             left.append(x)
#         if x <pivot:
#             right.append(x)
#         else:
#             mid.append(x)
#     return quick___sort(left) + mid + quick___sort(right)

# print(arr)


