def fec(n):
    if(n==1 or n==0):
        return 1 
    return n*fec(n-1)
    

a=fec(int(input()))
print(a)