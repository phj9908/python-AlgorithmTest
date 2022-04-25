# 1946 간단한 압축 풀기

#문자열 변수 하나에 입력할 문자열 싹 넣은뒤 길이 10만큼 잘라 출력
tc = int(input())
for t in range(1, 1+tc):
    n = int(input())
    arr = ''
    for _ in range(n):
        word, number = input().split()
        arr += word*int(number)

    print(f'#{t}')
    for i in range(0, len(arr), 10):
        print(arr[i:i+10])