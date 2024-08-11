def great(a,b,c):
    if(a>b):
        if(a>c):
            print(f"{a} is greatest")
        else:
            print(f"{c} is greatest")
    elif(b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")



great(int(input()),int(input()),int(input()))