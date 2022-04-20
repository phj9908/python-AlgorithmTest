# 문자열 압축(다시풀어보기)

def solution(s):
    answer=[]
    for step in range(1,len(s)//2+1): # 압축할 길이
        prev=s[:step]
        word=''
        cnt=1
        for j in range(step,len(s),step): # 압축 단위마다 반복
            if s[j:j+step]==prev:
                cnt+=1
            else: # 다른 문자열이 나오면
                if cnt>=2: 
                    word+=str(cnt)+prev 
                else:
                    word+=prev
                cnt=1
                prev=s[j:j+step]  # 압축 단위 문자열 초기화 (aabb면 aa->bb), 남은 문자열이 aaa인데 step이 5라도 남은 두 자리는 null값으로 되어서 그냥 'aaa'됨

        # 남은 문자열 처리
        if cnt>=2: 
            word+=str(cnt)+prev
        else:
            word+=prev
        
        answer.append(len(word))
    return min(answer)
print(solution(input()))