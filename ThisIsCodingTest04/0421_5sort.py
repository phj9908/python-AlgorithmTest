# 안테나  ,다시풀어보기
# (오름차순 정렬한 뒤 중간값이 무조건 답)
n=int(input())
arr=sorted(list(map(int,input().split())))
answer=arr[(n-1)//2] # 홀수개 일땐 정답이 하나이지만 짝수개일 땐 정답이 두개임 근데 이땐 더 작은 값이 답이돼야하기에 (n-1)//2 하면 해결
print(arr[answer[0][1]])
    