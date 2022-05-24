# 1316 그룹단어 체커

n=int(input())
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            if word[i] in word[i+1:]:
                n-=1
                break
print(n)


