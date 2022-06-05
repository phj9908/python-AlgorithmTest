# 비밀지도
def solution(n, arr1, arr2):
    answer = [ [' ']*n for i in range(n)]
    for i in range(len(arr1)):
        a=bin(arr1[i])[2:]
        b=bin(arr2[i])[2:]
        arr1[i]=(n-len(a))*'0'+a
        arr2[i]=(n-len(b))*'0'+b

        for j in range(n):
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                answer[i][j]='#'

        answer[i]=''.join(answer[i])
    return answer

# 다른 방법
# rjust : 오른쪽으로 정렬,
# 문자열.rjust(전체 자리 숫자, 공백이 있을 경우 공백을 채울 텍스트)
#
# answer=[]
# for i,j in zip(arr1,arr2):
#     arr=str(bin(i|j)[2:])
#     arr=arr.rjust(n,'0')
#     arr=arr.replace('1','#')
#     arr=arr.replace('0',' ')
#     asnwer.append(arr)
#
# return arr