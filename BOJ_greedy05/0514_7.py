# 1541 잃어버린 괄호(북마크 부분 복습)

def fun1(word):
    arr=list(map(int,word.split('+')))
    return sum(arr)

def fun2(word):
    arr=list(map(int,word.split('-')))
    res=arr[0]
    for i in arr[1:]:
        res-=i
    return res

word=input() # ex) '50-50+50'
if '-' not in word:
    print(fun1(word))
    exit()

if '+' not in word:
    print(fun2(word))
    exit()

answer=word.split('-') # word가 list자료형이 아니어도 그냥 이렇게하면 ['50','50+50']으로됨
for i in range(len(answer)):
    if ('+' not in answer[i]) and ('-' not in answer[i]):
        answer[i]=int(answer[i])
        continue
    else:
        answer[i]=fun1(answer[i])

res=answer[0]
for i in answer[1:]:
    res-=i
print(res)
