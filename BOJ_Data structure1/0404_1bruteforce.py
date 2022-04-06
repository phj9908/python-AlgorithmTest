# 10972 다음순열
# https://ji-gwang.tistory.com/262 '다음순열' 알고리즘 이해!
# https://my-coding-notes.tistory.com/333 코드 참고
import sys

n=int(input())
num=list(map(int,input().split())) # 1432
swap=0

for i in range(len(num)-1,0,-1): # 뒤에서 부터 순회
    if num[i-1]<num[i]: # 앞칸보다 뒷칸이 클 경우
        swap=i-1 #앞칸의 인덱스 저장
        break
else: # 내림차순인 경우이므로
    print(-1)
    sys.exit()

for i in range(len(num)-1,0,-1): # 또 뒤에서부터 순회
    if num[i]>num[swap]: # swap인덱스보다 큰 값이 있으면
        num[i],num[swap]=num[swap],num[i] # 스왑
        num=num[:swap+1]+sorted(num[swap+1:]) # swap+1 인덱스부터 오름차순 정렬한뒤 앞부분과 이어붙이기
        print(*num)
        break
