r='abc,dfg,dfg'
arr=[]
arr=r.split(',')
hash={ name for name in arr}
print(hash)

# arr.append()로 했다가 [['James','Ace']]이래 됨. 결과적으로
#hash = {name: 0 for name in arr}에서  name='James'가 아닌 ['James']가 되어 TypeError: unhashable type: 'list' 뜸
