# 버블정렬 : 기본적으로 오름차순 정렬(=스캔:배열에서 가장 큰 값이 마지막 인덱스에 오도록함)
# 인접한 원소 2개씩 비교해서 모든 숫자가 정렬될 때까지 반복, 스캔 1회 때는 가장 큰 수가 맨 뒤에 위치됨. 스캔 2회 때는 두번째로 큰 수가 뒤에서 두번째 인덱스에...
# https://codemate.kr/project/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-Level-1/5-2.-%EB%B2%84%EB%B8%94-%EC%A0%95%EB%A0%AC
# O(n^2)
arr=[5,2,9,1,6]
len=len(arr)-1 # 실제로 자리바꿀지 비교하는 코드는 마지막에서 두번째 인덱스까지만 하니까

while len>1:
    for i in range(len):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]
    len-=1
print(*arr)