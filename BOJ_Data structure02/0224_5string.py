# 11655 ROT13

str= input()
res=''
for i in str:
    if i == ' ' or ord(i)<ord('A'): # 공백이나 숫자일 때 =i.isspace() or i.isdigit()
        res+=i # 그대로 출력
    elif i.isupper() and ord(i)+13>90:
        res+=chr(ord('A')+ (ord(i)+13)-90) 
    elif ord(i)+13>122:
        res+=chr(ord('a')+ (ord(i)+13)-122) 
    else:
        res+=chr(ord(i)+13)
print(res)
