# 17413 단어 뒤집기 2

import sys
word = list(sys.stdin.readline().rstrip())

idx=0 # 현재 인덱스

while idx < len(word):
    if word[idx] == '<':
        idx+=1
        while word[idx] !='>':
            idx+=1
        idx+=1
    elif word[idx].isalnum() : # 숫자나 알파벳이면
        start = idx
        while idx < len(word) and word[idx].isalnum():
            idx+=1
        reverse_word = word[start:idx] # 태그 외에 문자열들 
        reverse_word.reverse()
        word[start:idx]=reverse_word # 다시 넣기
    else : # 괄호,숫자, 알파벳이 아닌 공백일 때
        idx +=1

print(''.join(word))

