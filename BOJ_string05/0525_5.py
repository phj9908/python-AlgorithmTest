#20154 이구역의 승자는 누구야
# 토너먼트 형식-> 왼족부터 누적합 하기

hash={'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':3,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':3,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
word=input()
total=0

for i in range(len(word)):
    total+=hash[word[i]]
    total%=10

if total%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")

