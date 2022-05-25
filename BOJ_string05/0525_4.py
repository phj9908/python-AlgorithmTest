#10798 세로읽기
arr=[]
for i in range(5):
    word=input()
    arr.append(word+(15-(len(word)))*'.')
answer=''
for i in range(15):
    word=''
    for j in range(5):
        word+=arr[j][i]
    answer+=word
answer=answer.replace('.','')
print(answer)
