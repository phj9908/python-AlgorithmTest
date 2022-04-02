# 17298 오큰수 : 다시 풀어보기

# 인덱스 1로 시작
# 1.자신보다 인덱스가 클것  2. 자신보다 큰 수 일 것 3. 복수 있는경우 인덱스가 가장 작은 것
# 없으면 -1
# https://hooongs.tistory.com/329 참고

from collections import deque
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) # 3 5 2 7
stack = deque() # (값,인덱스)로 묶어서 할당할 것임
result=[-1]*n

for i in range(n):
    while stack and (stack[-1][0] < arr[i]): # 자신보다 더 큰값이 나타났을 때
        num, idx = stack.pop()
        result[idx] = arr[i]
    stack.append((arr[i],i))
print(*result) # 5 7 7 -1




                
