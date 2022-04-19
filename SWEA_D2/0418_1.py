# 10912. 외로운 문자
tc=int(input())
for t in range(1,tc+1):
    word=list(input())
    set_word=list(set(word))
    answer=[]
    res=''
    for i in range(len(set_word)):
        if (word.count(set_word[i]))%2==1:
            answer.append(set_word[i])
    if len(answer)==0:
        res='Good'
    else:
        answer=sorted(answer)
        res=''.join(answer)
    print(f'#{t} {res}')
    
    