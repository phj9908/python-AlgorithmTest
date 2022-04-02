#11653 : 소인수분해

n=int(input())
idx=2
while n>1:
    if n%idx ==0 :
        print(idx)
        n //= idx
    else:
        idx+=1
        