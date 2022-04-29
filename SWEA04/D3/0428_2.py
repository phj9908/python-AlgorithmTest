# 7675. 통역사 성경이
tc=int(input())
for t in range(1,tc+1):
    n=int(input()) # 문장 수
    word=input()
    end_spot='.!?'
    str=[]
    end=0
    for i in range(len(word)):
        if word[i] in end_spot:
            str.append(word[end:i])
            end=i

    answer=[0]*n
    for i in range(n): # i=문장
        name=list(str[i].split())
        for j in name: # j=단어
            for k in range(len(j)): # k=스펠링(인덱스)
                #name_k=j[k]
                #name_bool=name_k.isupper()
                if k==0 and not j[k].isupper(): # 첫글자가 대문자가 아니면
                    break
                #name_bool=j[k].isalpha()
                if k!=0 and not j[k].islower(): # 나머지글자가 소문자가 아니면
                    break
            else:
                answer[i]+=1
    
    print(f'#{t}',end=' ');print(*answer)
