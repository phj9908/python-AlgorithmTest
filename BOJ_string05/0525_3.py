#9046 복호화 ( Counter쓰면 틀림)
for _ in range(int(input())):
    word=input()
    answer=[0]*26 # 알파벳 갯수
    for i in word:
        if i.isalpha():
            answer[ord(i)-97]+=1 # ord('a')=97

    if answer.count(max(answer))>=2:
        print('?')
    else:
        print(chr(97+answer.index(max(answer))))



