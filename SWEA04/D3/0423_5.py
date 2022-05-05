# 4789. 성공적인 공연 기획
tc=int(input())
for t in range(1,tc+1):
    word=input()
    answer=0
    sum=0
    cnt=0
    if '0' in word:
        for i,v in enumerate(word):
            v=int(v)
            if i>sum:
                answer+= i -sum # 고용할 사람들
                sum+=(i-sum)+v # i인덱스까지 박수칠 사람들= (고용할 사람들)+i인덱스의 사람들
            else:
                sum+=v

    print(f'#{t} {answer}')
            
