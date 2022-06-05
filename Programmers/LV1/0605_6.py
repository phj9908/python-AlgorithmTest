# 같은 숫자는 싫어

def solution(arr):
    answer=[]
    for j in range(len(arr)-1):
        if arr[j]!=arr[j+1]:
            answer.append(arr[j])
    answer.append(arr[-1])
    return answer

# 다른 방법
# answer=[]
# for i in arr:
#     if answer[-1:]==[i]: # 주의 ! answer[-1]은 answer이 empty일 때 에러가 나기에 [-1:]로 해주기
#         continue
#     answer.append(i)
#
# return answer