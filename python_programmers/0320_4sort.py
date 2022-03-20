# 가장 큰수
# 요구사항에 따른 정렬+내림차순 >> sort(key= lambda x: ...,reverse= True)

def solution(numbers):
    
    numbers=[str(i) for i in numbers]
    numbers.sort(key=lambda x:x*3,reverse=True) 
    # 원소범위가 1000이하이기에 3자리수만큼 수를 만들어주고 그 상태에서 비교
    # 문자열 비교는 아스키코드로 변환되어 크기 비교

    if numbers[0]=='0': # 정렬을 했는데도 '0000'인 경우
        return '0'
    
    return ''.join(numbers) # 문자열 원소들 합쳐서 출력