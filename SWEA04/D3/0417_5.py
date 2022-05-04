# 4676. 늘어지는 소리 만들기

tc = int(input())

for t in range(1,tc+1):
    word = list(input())
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True) # 큰 인덱스 부터 삽입해줘야 뒤섞이지 않기에!!!!
    for i in arr:
        word.insert(i,'-') # insert(인덱스,넣을 원소)

    print(f'#{t}',end=' ');print(''.join(word))

# 내 풀이(스택 활용, 비효율적)
# tc=int(input())
# for t in range(1,tc+1):
#     word=list(input()) # ['w','o','w']
#     length=len(word)
#     n=int(input())
#     place=list(map(int,input().split()))
#     set_place=list(set(place))
#     cnt=[0]*len(set_place)
#     length+=len(set_place)
#     answer=''
    
#     for i in range(len(set_place)):
#         cnt[i]=place.count(set_place[i])
    
#     i=0
#     while i<length:
#         if i in set_place:
#             for j in range(len(set_place)):
#                 if i==set_place[j]:
#                     answer+='-'*cnt[j]
#         if len(word)!=0:
#             answer+=word.pop(0)
#         i+=1

#     print(f'#{t}',end=' ');print(answer)