# 2217 로프(다시풀기)
# arr=[27,23,15,11,3] 일 때
# 로프가 1개있다면 27까지만 들수 있고, 로프가 2개있다면 23*2의 중량까지 들수 있고...이 중량들중 최대중량 구하기

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=sorted(arr,reverse=True)
for i in range(n):
    arr[i]=arr[i]*(i+1)
print(max(arr))