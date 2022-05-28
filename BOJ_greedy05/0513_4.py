# 1343 폴리오미노(다시풀기)

# # 풀이1) replace()활용 : replace()는 왼쪽부터 해당문자열을 찾아 치환함.
# word=in.txt()
# word=word.replace('XXXX','AAAA') # 왼쪽부터 모든 'XXXX'를 찾아 'AAAA'로 치환한 뒤
# word=word.replace('XX','BB') # 바뀐 문자열에서 남은 'XX'를 'BB'로 치환
#
# if 'X' in word:
#     print(-1)
# else:
#     print(word)

# 풀이2) 'xxxx'냐 'xx'냐 '.'에 따라 다른 배열에 할당하기
word=input()
answer=[]
i=0
while i<len(word):
    if word[i:i+4]=='XXXX':
        answer.append('AAAA')
        i+=4
    elif word[i:i+2]=='XX':
        answer.append('BB')
        i+=2
    elif word[i]=='.':
        answer.append('.')
        i+=1
    else:
        break

if len(word)!=len(answer):
    print(-1)
else:
    print(''.join(answer))



# #내 풀이
# def fun(start_i,length):
#     global word
#
#     if length % 2 == 1:
#         print(-1)
#         exit()
#     if length >= 4:
#         if length % 4 == 0:
#             word[start_i:start_i + length] = ['A'] * 4 * (length // 4)
#         else:
#             word[start_i:start_i + length] = ['A'] * 4 * (length // 4) + ['B'] * 2
#     else:
#         word[start_i:start_i + 2] = ['B'] * 2
#
#     return
#
# word=list(in.txt())
# length=0
# start_i=-1
# if '.' in word:
#     for i in range(len(word)):
#         if word[i].isalpha():
#             if start_i==-1:
#                 start_i=i
#             length+=1
#         elif word[i]=='.' and length!=0:
#             fun(start_i,length)
#             start_i,length=-1,0
#     if start_i!= -1:
#         fun(start_i,length)
#
# else:
#     fun(0,len(word))
#
# print(''.join(word))