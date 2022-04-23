# 정답 써칭하기

tc=int(input())
for t in range(1,tc+1):
    word=input()
    answer=0
    sum=0
    cnt=0
    if '0' in word:
        for i,v in enumerate(word):
            if v=='0':
                cnt+=1
            
            if i!=0 and word[i-1]=='0' and word[i]!='0':
                if sum<i:
                    answer+=cnt
                cnt=0
            
            sum+=int(v)  

    print(f'#{t} {answer}')
            
