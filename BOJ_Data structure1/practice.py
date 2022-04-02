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