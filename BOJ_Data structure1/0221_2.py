# 1158 요세푸스 문제
# 굳이 일렬로 풀어서 생각하는것보다 원테이블로 이해하는게 나음
cnt, num =map(int,input().split()) # 7,3

josephus = [i for i in range(1,cnt+1)] # {1,2,3,4,5,6,7}
result=[]
idx= num-1 # 리스트 시작이 0이니까 -1 해주기
while len(josephus):
    if idx >=len(josephus) : # idx가 원 한바퀴 이상 넘었을때
        idx = idx%len(josephus) # 3명이서 5번때 순서를 정할 때 5%3=2 ->2번째사람 이 되는 원리
    else :
        result.append(str(josephus.pop(idx)))
        idx += num -1
print("<"+", ".join(result)+">") # ''.join(String[])로 각 원소랑 ', ' 문자열 합치기 # <3,6,2,7,5,1,4>
