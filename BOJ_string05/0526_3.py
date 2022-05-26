# 16171 나는 친구가 적다(small)

word=input()
key=input()
temp=''

for i in range(len(word)):
    if word[i].isalpha():
        temp += word[i]

if key in temp:
    print(1)
else:
    print(0)
