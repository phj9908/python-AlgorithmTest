#9093 단어뒤집기
import sys
sys_input = sys.stdin.readline().rstrip() # stdin.readline 특성상 입력되는 맨끝의 '\n'제거

t=int(sys_input)
for _ in range(t):
    words=[]
    words =sys.stdin.readline().rstrip().split() # {'i','am','happy'}
    reverse_words =[]
    for i in words: # i='am' 일 때
        reverse_words.append(i[::-1])
    print(*reverse_words)
    #result = ' '.join(reverse_words) # 마지막에 단어사이 공백 추가
    #print(result)

# 다른 방법 : 파이썬 내장함수(reversed(리스트))
# 삼중 for문 (sentence/word/char) reverse_arr += char 거꾸로 할당
