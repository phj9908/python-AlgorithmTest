# 11688. Calkin-Wilf tree 1
tc=int(input())

def tree(node,a,b):
    if len(node)==0:
        return a,b
    
    n=node.pop(0)
    if n=='L':
        return tree(node,a,a+b)
    else:
        return tree(node,a+b,b)


for t in range(1,tc+1):
    node=list(input())
    a,b=tree(node,1,1)

    print(f'#{t} {a} {b}')