# boj_bruteforce문제는 거의 다 다시봐야함
# 2309 일곱난쟁이

arr=[]
for i in range(9):
    arr.append(int(input()))
arr=sorted(arr)
s=[]

def dfs(start):
    global answer

    if len(s)==7:
        if sum(s)==100:
            for i in s:   # answer=s 해서 마지막에 출력하려 했으나 그렇게하면 answer이랑 s랑 연동되어서 answer까지 계속 바뀜
                print(i) 
            exit()
        return 
    for i in arr[start:]:
        if i not in s:
            s.append(i)
            dfs(arr.index(i))
            s.pop()

dfs(0)

# permutation ver.
# from itertools import permutations

# num= [int(input()) for _ in range(9)]
# per_list=permutations(num,2) # -> (3,5),(12,5) ...
# for i in per_list:
#     if sum(num) - sum(i) == 100:
#         num.remove(i[0])
#         num.remove(i[1])
# num=sorted(num)
# for n in num:
#     print(n)