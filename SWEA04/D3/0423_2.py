# 3809. 화섭이의 정수 나열 (다시 풀어보기)
tc=int(input())
for t in range(1,tc+1):
    n=int(input())

    # 입력받는 수 문자열 하나로 만들기 (방법1)
    # for i in range(len(arr)):
    #     arr[i]=str(arr[i])
    # arr=''.join(arr)

    #                            (방법2)
    word=''
    while 1:
        word+=''.join(input().split()) # 입력이 한줄이거나 여러줄일수도 있기에 while로 받고 
        if len(word)==n:               # n자리 채우면 입력 끝
            break

    count=0
    answer=0
    while 1:
        if str(count) not in word:
            answer=count
            break
        count+=1
    print(f'#{t} {answer}')


# 재귀로 풀기 (샘플 테케만 맞음..)
# import sys
# import math
# stdin=open('input.txt')

# def dfs(start,k):
#     global answer

#     if start==n:
#         for i in range(10**(k-1),10**k):
#             if i not in s:
#                 answer=i
#                 return
#         k+=1
#         start=0
        
#     str=arr[start:start+k]
#     str=int(''.join(str))
#     if str not in s:
#         s.append(str)
#     dfs(start+1,k)

# tc=int(input())
# for t in range(1,tc+1):
#     #n=int(input())
#     n=100
#     arr=[]
#     for i in range(math.ceil(n/20)):
#         arr+=list(stdin.readline().strip().split())
#     s=[]
#     answer=0

#     dfs(0,1)
#     print(f'#{t} {answer}')
