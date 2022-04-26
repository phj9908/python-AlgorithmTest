# (백준 1439)문자열 뒤집기(다시풀어보기)
word=input()
cnt0=0 # 모두 0으로 바꾸는 경우
cnt1=0 # 모두 1로 바꾸는 경우

for i in range(len(word)-1):
    if word[i]!=word[i+1]:
        if word[i]=='0':
            cnt0+=1
        else:
            cnt1+=1
print(min(cnt0,cnt1))