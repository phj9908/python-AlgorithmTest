# 10809 알파벳 찾기

str=input()
arr=[]
for i in range(ord('Z')-ord('A')+1):
    arr.append(-1)
for i in range(len(str)):
    if str[i] not in str[:i]: # 각 알파벳의 처음등장하는 인덱스 할당
        arr[ord(str[i])-ord('a')]=i
    else:
        continue
print(*arr)
    
