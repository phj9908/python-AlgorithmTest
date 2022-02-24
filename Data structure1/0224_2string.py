#10808

str=input()
arr=[]
for i in range(ord('Z')-ord('A')+1):
    arr.append(0)
for i in str:
    arr[ord(i)-ord('a')]+=1
print(*arr)