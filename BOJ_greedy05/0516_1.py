# 2812 크게만들기 (다시 풀기)
n,k =map(int,input().split())
num=list(input())
stack=[]

for i in range(n):
    while stack and k>0 and stack[-1]<num[i]: # 앞의 숫자보다 지금숫자가 더 클 때
        stack.pop() # 앞의 숫자 제거
        k-=1
    if k==0:
        stack+=num[i:] # 지금 num부터 마지막 숫자까지 원소를 stack에 추가(append와 다름 주의!!)
        break
    stack.append(num[i])
if k>0:
    stack=stack[:-k] # k가 남았지만 내림차순 정렬이 된경우, 뒤에서부터 k개 제거
print(''.join(stack))
