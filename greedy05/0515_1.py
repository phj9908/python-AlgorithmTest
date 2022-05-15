# 13164 행복유치원 (다시풀기 )
# https://fullalgorithmpanic.blogspot.com/2016/10/boj-13164.html 밑에서 5번째 줄부터 참고
# n명의 학생들을 k개의 그룹으로 나눈다 = k-1개의 경계가 있음
# 인접한 사람끼리(2명을 말하는거임!!) 키차이를 배열에 할당후 오름차순 정렬

n,k=map(int,input().split())
arr=list(map(int,input().split()))
dif=[]
for i in range(len(arr)-1):
    dif.append(arr[i+1]-arr[i])
dif.sort()
for i in range(k-1):
    dif.pop()
print(sum(dif))
