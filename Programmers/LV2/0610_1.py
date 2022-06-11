# 뉴스 클러스터링
# Counter함수를 이용한 다중집합의 합집합,교집합 구현 ver.
# Counter함수는 set()함수와 마찬가지로 집합구조로 생성가능하다!
from collections import Counter

def solution(str1,str2):
    arr1=[ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2=[ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    # 아래 코드를 단축시킴
    # arr1,arr2=[],[]
    # for i in range(len(str1) - 1):
    #     if str1[i].isalpha() and str1[i + 1].isalpha():
    #         arr1.append(str1[i:i + 2].lower())
    # for i in range(len(str2) - 1):
    #     if str2[i].isalpha() and str2[i + 1].isalpha():
    #         arr2.append(str2[i:i + 2].lower())

    Counter1=Counter(arr1)
    Counter2=Counter(arr2)

    # 집합구조 만들기
    inter_arr=list((Counter1&Counter2).elements()) # elements()를 이용해서 key값만 뽑기
    union_arr=list((Counter1|Counter2).elements())
    # >> inter_arr=['fr', 'nc']
    # >> union_arr=['fr', 'ra', 'an', 'nc', 'ce', 're', 'en', 'ch']

    if len(union_arr)==0 and len(inter_arr)==0:
        return 65536
    else:
        return int(len(inter_arr)/len(union_arr)*65536)

#------------------------------------------------------------------------------
# set(),min(),max()이용 ver.
def solution2(str1,str2):
    arr1=[ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2=[ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    inter_arr=set(arr1) & set(arr2)
    union_arr=set(arr1) | set(arr2)

    if len(union_arr)==0:
        return 65536

    inter_sum=sum([min(arr1.count(i),arr2.count(i)) for i in inter_arr])
    union_sum=sum([max(arr1.count(i),arr2.count(i)) for i in union_arr])

    return int(inter_sum/union_sum)*65536

# -------------------------------------------------------------------------------
# 다중집합(중복허용 집합)의 합집합,교집합 https://codingpractices.tistory.com/48
# def solution2(str1, str2):
#    arr1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
#    arr2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
#
#     # 교집합 구하기
#     g_arr,arr=[],arr1.copy()
#     for i in arr2:
#         if i in arr:
#             arr.remove(i)
#             g_arr.append(i)
#
#     # 합집합
#     s_arr,arr=arr1.copy(),arr1.copy()
#     for i in arr2:
#         if i not in arr:
#             s_arr.append(i)
#         else:
#             arr.remove(i)
#
#     #print(g_arr)
#     #print(s_arr)
#     if not g_arr and not s_arr:
#         return 65536
#
#     return int((len(g_arr)/len(s_arr))*65536)

