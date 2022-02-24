# 11655

str= input()
res=''
for i in str:
    if i == ' ' or ord(i)<ord('A'): # 공백이나 숫자일 때
        res+=i
    elif i.isupper() and ord(i)+13>90:
        res+=chr(64+ (ord(i)+13)-90) # 'A'=64
    elif ord(i)+13>122:
        res+=chr(96+ (ord(i)+13)-122) # 'a' = 96
    else:
        res+=chr(ord(i)+13)
print(res)
