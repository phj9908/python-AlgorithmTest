# 2812 크게만들기 (다시 풀기)
n,k =map(int,input().split())
num=list(input())
_k,stack=k,[]

for i in range(n):
    while stack and _k>0 and stack[-1]<num[i]: # 앞의 숫자보다 지금숫자가 더 클 때
        stack.pop() # 앞의 숫자 제거
        _k-=1
    stack.append(num[i])

print(''.join(stack[:n-k])) # k가 남았지만 내림차순 정렬이 된경우, 뒤에서부터 k개 제거
