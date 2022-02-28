#2745 진법변환: b진법 수를 10진수로 바꾸기
n,b = input().split()
b= int(b)
tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res=0

for i in range(len(n)):
    res+=tmp.index(n[i])*(b**(len(n)-1-i))

print(res)