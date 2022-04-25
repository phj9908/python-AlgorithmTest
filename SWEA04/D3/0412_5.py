# 1215. 회문

def check(word): 
    while len(word)>0:
        if len(word)==1:
            return True
        if word[0]==word[-1]:
            word.pop(0)
            word.pop()
        else:
            return False
    return True


for t in range(1,11):
    n=int(input())
    arr=[ list(input()) for _ in range(8)]
    answer=0

    for i in range(8):
        for j in range(8-n+1):
            word=list(arr[i][j:j+n])
            if check(word): # or 'if word==word[::-1]'
                answer+=1
        for j in range(8-n+1):
            word=[]
            for w in range(n):
                word.append(arr[j+w][i])
            if check(word):
                answer+=1
    
    print(f'#{t} {answer}')
