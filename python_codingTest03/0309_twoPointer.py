# 투 포인터
# 일차원 리스트에서 두 개의 포인터를 조작
#https://codemate.kr/project/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-Level-1/8-1.-%ED%88%AC-%ED%8F%AC%EC%9D%B8%ED%84%B0%EC%99%80-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9-%EC%9C%88%EB%8F%84%EC%9A%B0 그림보기

n=int(input()) # 원소 갯수
arr= list(map(int,input().split())) 
m=int(input()) # 찾으려는 합 값

start,end=0,0
partial_sum=0
answer =0

while start< n:

    if partial_sum>m or end>= n: # 배열합이 목표값보다 크거나 end가 배열 끝에 도달했을 때
        partial_sum -= arr[start]
        start +=1

    elif partial_sum <= m: 
        partial_sum += arr[end]
        end +=1

    if partial_sum==m:
        print(arr[start:end],start,end)
        answer+=1

print(answer)
