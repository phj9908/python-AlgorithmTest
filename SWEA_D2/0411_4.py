#1928. Base64 Decoder : 64진수(=6비트=2^6) 글자들을 8비트 글자로 변환
# https://swbeginner.tistory.com/entry/SWEA-%EC%BD%94%EB%94%A9-Base64-Decoder-PYTHON-1928
# TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u -> Life itself is a quotation.

decoder_arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

tc=int(input())
for t in range(1,tc+1):
    scr=input()
    temp=''
    answer=''
    for c in scr:
        to_binary=bin(decoder_arr.index(c))[2:] # 이진수로 변환(0b생략)
        if len(to_binary) < 6: 
            to_binary ='0'*(6-len(to_binary)) +to_binary # 6자리가 될때 까지 0을 앞에!! 붙인다
        temp+=to_binary
    for i in range(0,len(temp),8): # 이진수를 8비트 단위로 자르기
        answer+=chr(int('0b'+temp[i:i+8],2)) # 그 이진수 십진수로 변환(int(,2))한 뒤 아스키코드로 변환(chr())
    
    print(f'#{t} {answer}')

# base64라이브러리 이용ver
# from base64 import b64decode

# tc=int(input())
# for t in range(1,tc+1):
#     word=input()
#     answer=b64decode(word).decode('UTF-8')

#     print(f'#{t} {answer}')

