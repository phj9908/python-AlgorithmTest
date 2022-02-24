# 10809

str=input()
arr=[]
for i in range(ord('Z')-ord('A')+1):
    arr.append(-1)
for i in range(len(str)):
    if str[i] not in str[:i]:
        arr[ord(str[i])-ord('a')]=i
    else:
        continue
print(*arr)
    
