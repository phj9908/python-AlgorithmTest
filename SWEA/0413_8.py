#4751. 다솔이의 다이아몬드 장식
tc=int(input())
for t in range(1,tc+1):
    word=input()
    res_word=''
    for w in word:
        res_word+='#.'+w+'.'
    res_word+='#'
    answer=[['']*len(res_word) for i in range(5)]

    for i in range(5):
        if i==2:
            answer[i]=res_word
        elif i%2!=0:
            answer[i]='.#.#'*len(word)+'.'
        else:
            answer[i]='..#.'*len(word)+'.'

    for i in answer:
        print(i)

