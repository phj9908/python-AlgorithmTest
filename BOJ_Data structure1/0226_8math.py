#1373 이진수를 8진수로 변환

n=int(input(),2) # 2진수를 입력받겠다 ( int()의 두번째인자 값은 defalut가 10)
print(oct(n)[2:]) # oct():8진수로 변환 / 답안에는 숫자만 표기해야 하므로 앞에 붙는 8진수를 알려주는 문자 '0o' 제외하기
# hex() : 16진수로 변환