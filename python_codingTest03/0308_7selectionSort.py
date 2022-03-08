# 선택 정렬
# 리스트 중 최솟값 찾아 첫 번째 인덱스와 스왑
# 이후 두번째 인덱스 부터 최솟값 찾아 또 두번째 인덱스와 교환...반복

arr=[9,6,7,3,5]
cnt_idx=0
max_idx=len(arr)-2

while cnt_idx<=max_idx:
    arr_tail=arr[cnt_idx:]
    min_idx=arr.index(min(arr_tail))
    arr[cnt_idx],arr[min_idx]=arr[min_idx],arr[cnt_idx]
    print(*arr)
    cnt_idx+=1


