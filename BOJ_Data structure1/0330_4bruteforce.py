# 1107 리모컨

n=int(input())
button_num=int(input())
answer=abs(n-100) # 숫자 버튼 안쓰고 +1 버튼만 누른 경우
if button_num: # button_num>0
    err_button= set(input().split())
else:
    err_button=set()

for channel_num in range(1000001): # 채널은 500,000까지 지만 만약 500,000로 이동하려는데 가능한 버튼이 9만 있으면 999,999에서 시작해야하니까
    for cha in str(channel_num):
        if cha in err_button: # 해당 숫자가 번호를 눌러서 만들수 없을 때
            break
    else:
        answer= min(answer,len(str(channel_num))+abs(channel_num-n))

print(answer)





