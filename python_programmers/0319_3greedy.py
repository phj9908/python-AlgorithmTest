# 조이스틱
#https://bellog.tistory.com/152 

def solution(name):
    answer=0
    min_move=len(name)-1
    next=0

    while name[min_move]=='A' and min_move>0: # 마지막에 A가 연속으로 있을 경우 대비
        min_move-=1

    if min_move <0:
        return answer

    for char in name:
        answer+=min(ord(char)-ord('A'), ord('Z')+1-ord(char)) # up과 down중 했을 때 더 작은 횟수
    for i in range(len(name)):
        next= i+1
        while next < len(name) and name[next]=='A': # 마지막 A의 인덱스(주의!! 조건에서 next < len(name) 먼저 앞에 안두면 인덱스 에러 발생)
            next +=1 # 마지막 A 다음 문자의 인덱스
        distance = min(i,len(name)-next)
        min_move=min(min_move,distance+i+(len(name)-next)) # 이해 부족
    answer+=min_move

    return answer