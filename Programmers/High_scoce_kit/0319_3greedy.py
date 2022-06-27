# 조이스틱
#https://bellog.tistory.com/152 

def solution(name):
    answer=0
    min_move=len(name)-1

    while name[min_move]=='A' and min_move>0: # 마지막에 A가 연속으로 있을 경우 대비
        min_move-=1

    if min_move <0:
        return answer

    for i,char in enumerate(name):
        answer+=min(ord(char)-ord('A'), ord('Z')+1-ord(char)) # up과 down중 했을 때 더 작은 횟수

        next= i+1
        while next < len(name) and name[next]=='A':
            next +=1 # 마지막 A 다음 문자의 인덱스 ('JAAZ'면 i=0일 때 next=3까지 채우고 반복문 탈출)
        min_move=min(min_move,i+i+(len(name)-next)) # 블로그 참고, 정방향으로 갔을때 vs 역방향으로 갔을 때
    answer+=min_move

    return answer