# 2309 일곱난쟁이
from itertools import permutations

num= [int(input()) for _ in range(9)]
per_list=permutations(num,2) # -> (3,5),(12,5) ...
for i in per_list:
    if sum(num) - sum(i) == 100:
        num.remove(i[0])
        num.remove(i[1])
num=sorted(num)
for n in num:
    print(n)