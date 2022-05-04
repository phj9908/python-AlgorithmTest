for t in range(1,int(input())+1):
      length=int(input())
      arr=list(map(int,input().split()))
      com_n=int(input())
      command=list(input().split())

      for i in range(len(command)):
          if command[i]=='I':
              x=int(command[i+1])
              y=int(command[i+2])
              s=command[i+3:]
              for j in range(y):
                  arr.insert(x+j,s[j])
          if command[i]=='D':
              x=int(command[i+1])
              y=int(command[i+2])
              for j in range(y):
                  del arr[x]
          if command[i]=='A':
              y=int(command[i+1])
              s=command[i+2:]
              for j in range(y):
                  arr.append(s[j])

