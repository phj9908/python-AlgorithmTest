#20365 블로그2 (다시풀기)
# ex) BBRRRBB

n=int(input())
arr=input()
b_cnt,r_cnt=1,1 # 모두 b로 덮인 경우, 모두 r로 덮인 경우

i=0
start_i=-1
while i<len(arr):
    if arr[i]=='R':
        if start_i==-1:
            start_i=i
            b_cnt+=1
    if arr[i]=='B':
        start_i=-1
    i+=1

i=0
start_i=-1
while i<len(arr):
    if arr[i]=='B':
        if start_i==-1:
            start_i=i
            r_cnt+=1
    if arr[i]=='R':
        start_i=-1
    i+=1
print(min(b_cnt,r_cnt))

