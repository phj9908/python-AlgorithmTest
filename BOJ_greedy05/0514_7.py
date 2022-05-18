# 1541 잃어버린 괄호(문자열 헷갈려했으니까 다시풀어보기)

def fun1(word):
    arr=list(map(int,word.split('+')))
    return sum(arr)

def fun2(word):
    arr=list(map(int,word.split('-')))
    res=arr[0]
    for i in arr[1:]:
        res-=i
    return res

word=input()
if '-' not in word:
    print(fun1(word))
    exit()

if '+' not in word:
    print(fun2(word))
    exit()

answer=word.split('-')
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
