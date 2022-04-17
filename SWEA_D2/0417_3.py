# 11856. 반반
tc=int(input())

for t in range(1,tc+1):
    word=list(input())
    
    set_word=list(set(word))
    if len(set_word)!=2:
        answer='No'
    else:
        err=0
        for i in range(2):
            if word.count(set_word[i])!=2:
                answer='No'
                err+=1
        if err==0:
            answer='Yes'   
    print(f'#{t} {answer}')