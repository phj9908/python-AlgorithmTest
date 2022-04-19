# 문자열 재정렬
word=input()
sum=0
answer=[]
for i in word:
    if i.isdigit():
        sum+=int(i)
    else:
        answer.append(i)
answer=''.join(sorted(answer))
answer+=str(sum)
print(answer)