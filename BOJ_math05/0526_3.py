# 1110 더하기사이클 (다시 풀기, 이거 카테고리 수학입!!)
num=input()
n=int(num)
cnt=0
while 1:
    cnt+=1
    word=str(n%10)+str(n//10+n%10)[-1]
    n=int(word)
    if int(num)==n:
        break

print(cnt)

