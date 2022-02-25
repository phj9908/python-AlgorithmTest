#11656

str= input() 
str_list=[]

for i in range(len(str)):
    str_list.append(str[i:])
str_list.sort()    
for i in str_list:
    print(i)