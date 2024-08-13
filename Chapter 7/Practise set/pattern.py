def pat(n):
    if(n==0):
        return
    print("*"*n)
    pat(n-1)

pat(int(input()))