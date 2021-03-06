# 전화번호 목록 : 배열이 '123','1234','1954' 일때, 접두사가 있으면 false./ '345' '254' '674' 는 True
#hash 의 빠른 탐색시간을 이용

def solution(phone_book):
    hash_table={}

    for i in phone_book:  # key-value 쌍 생성목적으로 일단 아무 value 할당
        hash_table[i]=1
    for i in phone_book:
        str=''
        for j in i:
            str+=j
            if str in hash_table.keys() and str != i:
                return False
    return True

# # 다른 풀이 1(zip,startswith이용)
# def solution(phonebook):
#     phonebook=sorted(phonebook)

#     for p1,p2 in zip(phonebook,phonebook[1:]): # 맨앞 원소 문자열이 다른 원소 문자열의 맨앞에 있는지 보는거니까
#         if p1.startswith(p2): #p2가 p1의 맨앞에 있다면
#             return False
#     return True