# 2559 수열(다시 풀기)
# 그냥 슬라이딩 윈도우식으로 하면 시간초과됨, sum 호출횟수가 많음 ,즉 더하기 연산을 다른 연산으로 바꿔야함
length, n=map(int,input().split())
arr=list(map(int,input().split()))

temp_list=[sum(arr[:n])]
for i in range(1,len(arr)-n+1):
    sum=temp_list[-1] + arr[i+n-1]-arr[i-1]
    # 다음 연속된 온도의 합 = 바로 이전 연속된 온도의 합 + 다음 순번에서 n번째 온도 - 이전 연속된 날짜 중 제일 최근의 온도
    # i==1 일때 해당하는 연속된 온도의 합은 -2 + -4 =-6 임,
    # 이때 여기서 -2는 바로이전 연속된 온도의 함 3 + (-2) =1 에서 3을 우항으로 이동시켜 -2대신 1-3 을 연산에 이용

    temp_list.append(sum)

print(max(temp_list))


# start,end=0,0
# sum_arr=[]
# while end<=length:
#     sum_arr.append(sum(arr[start:end]))
#     start+=1
#     end = start + n
# print(max(sum_arr))

