#12933 오리 (다시풀기) https://eboong.tistory.com/288
# for문을 돌리면서 배열수정을 해야할 때 -> 방문유무 체크 배열 만들기!!

word=list(input())
quack='quack'
visited=[False]*len(word)
first=False # 첫써클 유무 파악
cnt=0
if len(word)%5!=0:
    print(-1)
    exit()

for i in range(len(word)):
    if word[i]=='q' and not visited[i]:
        first=True
        idx=0 # quack의 인덱스
        for j in range(len(word)):
            if word[j]==quack[idx] and not visited[j]:
                visited[j]=True
                if word[j]=='k':
                    if first:
                        cnt+=1
                        first=False
                    idx=0
                    continue
                idx+=1
if cnt==0 or all(visited)!=True: # 써클 돈적이 없거나 visited에 false가 하나라도 있을 때
    print(-1)
else:
    print(cnt)