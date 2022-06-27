# 체육복 : 
# 자기번호 +-1 번호들에게 빌려줄수있음

# 학생수 30명,학생마다 체육복 수 1씩 할당하고 시작
def solution(n, lost, reserve):
    
    students=[1]*(n+2) # 1번~n번 외에 0번,n+1번에도 1할당
    for i in reserve:
        students[i]+=1 
    for i in lost:
        students[i]-=1 # reserve,lost 둘 다 속한 학생은 다시 1이 되도록
         
    for i in range(1,n+1):
        
        if students[i-1] ==0 and students[i] ==2:
            students[i-1:i+1]=[1,1]
        elif students[i+1] ==0 and students[i] ==2:
            students[i:i+2]=[1,1] # 인덱스 i,i+1은 1 저장    

    return len([x for x in students[1:-1] if x>0]) # 1번 부터 n번 중에서 1의 값을 갖는 학생의 수 반환 (마지막에서 두번째는 인덱스로 -2임 따라서 [1:-1])

# # 다른풀이(set,교집합 이용)
# def solution(n, lost, reserve):
#     s=set(lost)&set(reserve) # lost와 reserve둘다 속한 사람
#     l_stu= set(lost)-s
#     r_stu=set(reserve)-s
    
#     r_stu=sorted(r_stu) # 오름차순 정렬
    
#     for i in r_stu:
#         if i-1 in l_stu:
#             l_stu.remove(i-1)
#         elif i+1 in l_stu:
#             l_stu.remove(i+1)
            
#     return n-len(l_stu)