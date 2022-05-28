# 1748 수 이어쓰기1
# 규칙 찾기!
# 1-9까지 숫자 연결하면 한자리 수가 9개니까 1*9
# 10-99                두자리      90개    2*90
# 100-999              세          900     3*900

# 99를 100-1로 계산.
num=input()
length=len(num)

ans=0
if length==1:
    print(length)
else:
    while length>1: 
        if length==len(num):
            ans+=(int(num)-((10**(length-1))-1))*length 
        else:
            ans+=(((10**length)-1)-(10**(length-1)-1))*length
        length-=1
    ans+=9
    print(ans)


# 아래 코드는 메모리초과
# num = int(in.txt())
# str_num=[ str(i) for i in range(1,num+1)]
# str_num=''.join(str_num)
# print(len(str_num))
