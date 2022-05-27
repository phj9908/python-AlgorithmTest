for i in range(int(input())):
    time=input()
    y,m,d=int(time[:4]),int(time[4:6]),int(time[6:])


    if 0>=m or m>=13 or 0>=d or 31<d:
        print(-1)
        continue

    if m==1:
        if d>31:
            print(-1)
            continue
    if m==2 and d>30:
        print(-1)
        continue
    if m==3 and d>31:
        print(-1)
        continue

