#17299 오등큰수 : 다시 풀어보기

# 1.자신보다 인덱스가 클것  2. 자신보다 등장횟수가 더 큰 수 일 것 3. 복수 있는경우 인덱스가 가장 작은 것
# Counter클래스 이용
# dictionary 구조로 각 원소의 진도수 도출 
# Counter('hello') : Counter({'h':1,'e':1,'l':2,'o':1})

from collections import Counter 
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split())) 
nums_cnt = Counter(nums) # Counter 딕셔너리 생성
stack = [] # nums인덱스 할당용
result=[-1]*n

for i in range(n):
    while stack and (nums_cnt[nums[stack[-1]]] < nums_cnt[nums[i]]): # 더 큰 빈도 값이 나타났을 때
        result[stack.pop()] = nums[i]
    stack.append(i)
print(*result) # -1 -1 1 2 2 1 -1