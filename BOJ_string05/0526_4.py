#9342 염색체

for _ in range(int(input())):
    word=input()
    a= word.find('A') # find() : 찾는 문자열이 없으면 -1출력
    f= word.find('F')
    c= word.find('C')
    err=False

    if a<0 or f<0 or c<0 or a>f or a>c or f>c:
        err=True

    if err or word[0] not in 'ABCDEF':
        err=True

    if not err:
        for i in range(a,f):
            if word[i]!='A':
                err=True
                break
    if not err:
        for i in range(f,c):
            if word[i]!='F':
                err=True
                break

    if err or word[-1] not in 'ABCDEF':
        err=True

    if err:
        print('Good')
    else:
        print('Infected!')

