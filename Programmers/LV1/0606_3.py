# 시저암호
def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper() and ord(s[i])+n>90:
                answer += chr(ord(s[i]) + n-26) # 알아두기 : ord('Z')-(ord('A')-1)=26
            elif s[i].islower() and ord(s[i])+n>122:
                answer += chr(ord(s[i]) + n -26)
            else:
                answer += chr(ord(s[i]) + n)
        else:
            answer+=' '
    return answer
print(solution('AB',1))