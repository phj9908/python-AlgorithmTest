# 영준이의 카드찾기
tc=int(input())
for t in range(1,tc+1):
    word=input()
    arr={'S':13,'D':13,'H':13,'C':13}
    word_arr=[]

    for i in range(0,len(word),3):
        w=word[i:i+3]
        word_arr.append((w[0],''.join(w[1:])))
        arr[w[0]]-=1

    set_arr=list(set(word_arr))
    
    if len(set_arr)!=len(word_arr):
        answer='ERROR'
    else:
        answer=str(arr['S'])+' '+str(arr['D'])+' '+str(arr['H'])+' '+str(arr['C'])
    print(f'#{t} {answer}')
    

