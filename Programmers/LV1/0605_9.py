# 행렬의 덧셈( 다시풀기 )

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr=[]
        for j in range(len(arr1[i])):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    return answer

# 또는

def solution2(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A