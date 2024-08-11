n=int(input())
print("")
for i in range(1,n+1):
    print("1"*i)
print("")
for i in range(1,n+1):
    print(" "*(n-i)+"1"*((i*2)-1))
print("")
for i in range(1,n+1):
    if(i==1 or i==n):
        print("1"*n)
    else:
        print("1"+" "*(n-2)+"1")
