def solution(n, plans, clients):
    answer = [0]*len(clients)
    add_plan=[]
    plan= {}
    plan_idx={}
    for px in plans:
        p=list(map(int,px.split()))
        idx=p[0]
        service=p[1:]
        plan[idx]=list(set(service)|set(sum(add_plan,[])))
        plan_idx[idx]=plans.index(px)
        add_plan.append(plan[idx])

    for cx in clients:
        c=list(map(int,cx.split()))
        for k in plan.keys():
            if c[0]<=k:
                for i in c[1:]:
                    if i not in plan[k]:
                        break
                else:
                    answer[clients.index(cx)]=plan_idx[k]+1
                    break

    return answer
