# 1343 폴리오미노
def fun(start_i,length):
    global word

    if length % 2 == 1:
        print(-1)
        exit()
    if length >= 4:
        if length % 4 == 0:
            word[start_i:start_i + length] = ['A'] * 4 * (length // 4)
        else:
            word[start_i:start_i + length] = ['A'] * 4 * (length // 4) + ['B'] * 2
    else:
        word[start_i:start_i + 2] = ['B'] * 2

    return

word=list(input())
length=0
start_i=-1
if '.' in word:
    for i in range(len(word)):
        if word[i].isalpha():
            if start_i==-1:
                start_i=i
            length+=1
        elif word[i]=='.' and length!=0:
            fun(start_i,length)
            start_i,length=-1,0
    fun(start_i,length)

else:
    fun(0,len(word))

print(''.join(word))