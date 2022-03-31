# 1748 수 이어쓰기1
# 아래 코드는 메모리초과
# num = int(input())
# str_num=[ str(i) for i in range(1,num+1)]
# str_num=''.join(str_num)
# print(len(str_num))

# 규칙 찾기!
# 1-9까지 숫자 연결하면 한자리 수가 9개니까 1*9
# 10-99                두자리      90개    2*90
# 100-999              세          900     3*900

num=input()
len=len(num)
ans=0
answer=0
if len==1:
    print(num)
else:
    while len>0:
        if answer==0:
            x=int(str((len-1)*'9'))
            ans=(int(num)-x)*len
        else:
            if len-1>0:
                ans=(int(str(len*'9'))-int(str((len-1)*'9')))*len
            else:
                ans=9
        len-=1
        answer+=ans

    print(answer)

# 다른 풀이
# n = input()
# n_len = len(n) - 1
# c = 0
# i = 0
# while i < n_len: # n-1자리수 까지 총 자리수 합
#     c += 9 * (10 ** i) * (i + 1)
#     i += 1
# c += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1) # n자리수 숫자 따로 계산, 99를 100-1로 계산.
# print(c)