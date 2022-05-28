#20436 ZOAC 3

# hash ver.
l,r=input().split()
word=input()
keyboard=['qwertyuiop','asdfghjkl','zxcvbnm'] # 굳이 [ ['q','w','e','r'...], ['a','s',..], ] 로 쓰지마라..
r_keyboard='yuiophjklbnm'
hash={}
for i in range(3):
    for j in range(len(keyboard[i])):
        hash[keyboard[i][j]]=(i,j)
ly,lx=hash[l]
ry,rx=hash[r]

total=0
for w in word:
    y,x=hash[w]
    if w not in r_keyboard:
        total+=abs(ly-y)+abs(lx-x)+1 # 거리 + 누르는 시간 1초
        ly,lx=y,x
    else:
        total+=abs(ry-y)+abs(rx-x)+1
        ry,rx=y,x
print(total)


# 배열ver.왜 틀렸는지 모르겠음
# l,r=in.txt().split()
# word=in.txt()
# l_y,l_x,r_y,r_x=0,0,0,0
# arr=[
#     'qertyuiop',
#     'asdfghjkl',
#     'zxcvbnm']
# right_keyboard='yuiophjklbnm'
#
# for i in range(3):
#     if l in arr[i]:
#         j=arr[i].index(l)
#         l_y,l_x=i,j
#     if r in arr[i]:
#         j=arr[i].index(r)
#         r_y,r_x=i,j
#
# total=0
# for w in word:
#     if w not in right_keyboard:
#         for i in range(3):
#             if w in arr[i]:
#                 j=arr[i].index(w)
#                 total+=abs(l_y-i)+abs(l_x-j)+1
#                 l_y,l_x=i,j
#     else:
#         for i in range(3):
#             if w in arr[i]:
#                 j = arr[i].index(w)
#                 total +=abs(r_y-i)+abs(r_x-j) + 1  # 거리 + 누르는 시간 1초
#                 r_y, r_x = i,j
# print(total)




