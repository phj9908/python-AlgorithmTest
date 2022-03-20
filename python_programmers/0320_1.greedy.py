#큰 수 만들기
def solution(number, k):
    
    collected=[] # 맨 앞부터 숫자 하나씩 담을 리스트
    for i,num in enumerate(number):
        while len(collected)>0 and collected[-1]<num and k>0: 
        # 리스트에 담았던 마지막 수 보다 num이 더크면
            collected.pop()
            k-=1
        if k==0: # 더 이상 수를 뺄 수 없을때
            collected+=number[i:] # 지금 num부터 마지막 숫자까지 더하기
            break
        collected.append(num)

    if k>0: # 9876같이 이미 내림차순 정렬 돼있으면
        collected=collected[:-k] # 뒤에서부터 k개 만큼 빼기
    answer = ''.join(collected) # 문자열 하나!로 반환하기 위함
    return answer