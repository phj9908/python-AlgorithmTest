# 21314 민겸수
word=list(input())
length=0
num=[]
i=0
while i<len(word):
    if word[i]=='M':
        length+=1
    else:
        num.append('5'+'0'*length)
        length=0
    i+=1
if length:
    num.append('1' * length)
answer=[int(''.join(num))]

i=0
length=0
num.clear()
while i<len(word):
    if word[i]=='M':
        if i+1<len(word) and word[i+1]=='M':
            length+=1
        else:
            if length:
                num.append('1'+'0'*length)
                length = 0
            else:
                num.append('1')
    else:
        num.append('5')
    i+=1
answer.append(int(''.join(num)))

for i in answer:
    print(i)



