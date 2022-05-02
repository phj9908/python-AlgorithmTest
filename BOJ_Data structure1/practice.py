word=list(input())
idx=0

while idx<len(word):
    if word[idx]=='<':
        idx+=1
        while idx<len(word) and word[idx]!='>':
            idx+=1
        idx+=1
    elif word[idx].isalnum():
        start=idx
        while idx<len(word) and word[idx].isalnum():
            idx+=1
        reverse_w=word[start:idx]
        reverse_w.reverse()
        word[start:idx]=reverse_w
    
    else:
    
        idx+=1
    
print(word)